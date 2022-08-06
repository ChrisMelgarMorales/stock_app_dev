
import json 
import pandas as pd 
from pandas.io.json import json_normalize 
from datetime import datetime
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
from Strategy import SmaCross
from SourceAdapter import Adapter,DirectAPI
import numpy



def handler(event, context):
  #get querry parameters
  day = event["queryStringParameters"]['day']
  month = event["queryStringParameters"]['month']
  year = event["queryStringParameters"]['year']
  funds = event["queryStringParameters"]['funds']
  strat = event["queryStringParameters"]['strategy']
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

  return {
      'statusCode': 200,
      'body': output.to_json(),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }