
import json 
import pandas as pd 
from pandas.io.json import json_normalize 
from datetime import datetime
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import numpy
class SmaCross(Strategy):
    n1 = 10
    n2 = 20

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

def handler(event, context):

  day = event["queryStringParameters"]['day']
  month = event["queryStringParameters"]['month']
  year = event["queryStringParameters"]['year']
  #Convert querry date to unix at 8am
  date_example = "{}/{}/{}, 08:00:0".format(day,month,year)
  s1 = datetime.strptime(date_example, "%d/%m/%Y, %H:%M:%S")
  period1 = int(s1.timestamp())
  #Convert current date to unix at 8am
  dateObj = datetime.now()
  date_example = "{}/{}/{}, 08:00:0".format(dateObj.day,dateObj.month,dateObj.year)
  s2 = datetime.strptime(date_example, "%d/%m/%Y, %H:%M:%S")
  period2 = int(s2.timestamp())

  symbol = event["queryStringParameters"]['stock']
  #read json data from yahoo querry
  data = pd.read_json("https://query1.finance.yahoo.com/v8/finance/chart/{sym}?symbol={sym}&period1={p1}&period2={p2}&interval=1d".format(sym = symbol,p1=period1,p2=period2))
  #set up data into relevant frames
  result = pd.DataFrame()
  result['Open'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['open'])
  result['High'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['high'])
  result['Low'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['low'])
  result['Close'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['close'])
  result['Volume'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['volume'])
  #run the backtest
  bt = Backtest(result, SmaCross,
              cash=10000, commission=.002,
              exclusive_orders=True)

  output = bt.run()

  return {
      'statusCode': 200,
      'body': output.to_json(),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }