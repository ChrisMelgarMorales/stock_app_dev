
import json 
import pandas as pd 
from pandas.io.json import json_normalize 
from datetime import datetime
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA

import numpy
#Strategy 1 for backtesting
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
class Adapter:
    """
    Adapts an object by replacing methods.
    """
 
    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)
 
    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)
 
    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__
#Class for producing backtesting data from yfinance
class YFinnance:
 
    """Class for MotorCycle"""
 
    def __init__(self):
        self.name = "yfin"
 
    def yfinData(self):
        return "TwoWheeler"
 
#class for producing Backtesting data in correct format from
#direct yahoo api request
class DirectAPI:

    def __init__(self,day,month,year):
        self.name = "direct"
        self.day = day
        self.month = month
        self.year = year
 
    def apiData(self):
        #Convert querry date to unix at 8am
        date_example = "{}/{}/{}, 08:00:0".format(self.day,self.month,self.year)
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
        return data

def handler(event, context):
  #get querry parameters
  day = event["queryStringParameters"]['day']
  month = event["queryStringParameters"]['month']
  year = event["queryStringParameters"]['year']
  funds = event["queryStringParameters"]['funds']
  strat = event["queryStringParameters"]['strategy']
  #Adapt Classes for getting data from yahoo to objects
  objects = []
  directAPI = DirectAPI(day,month,year)
  objects.append(Adapter(directAPI,getData = directAPI.apiData))
  data = objects[0].apiData()
  #set up data into relevant frames
  result = pd.DataFrame()
  result['Open'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['open'])
  result['High'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['high'])
  result['Low'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['low'])
  result['Close'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['close'])
  result['Volume'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['volume'])
  #run the backtest
  if strat.lower() == "smacross" :
    bt = Backtest(result, SmaCross,
              cash=int(funds), commission=.002,
              exclusive_orders=True)

    output = bt.run()
  #output results to json file
  return {
      'statusCode': 200,
      'body': output.to_json(),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }