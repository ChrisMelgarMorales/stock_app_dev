
import json 
import pandas as pd 
from pandas.io.json import json_normalize 
from datetime import datetime
from backtesting import Backtest, Strategy
from backtesting.lib import crossover,SignalStrategy, TrailingStrategy
from backtesting.test import SMA
import yfinance as yf
import numpy
#Strategy 1 for backtesting taken from Backtesting.py
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
#this class is taken from the ipynb docummentation of strategies for
#Backtesting.py
class SmaTrailCross(SignalStrategy,
               TrailingStrategy):
    n1 = 10
    n2 = 25
    
    def init(self):
        # In init() and in next() it is important to call the
        # super method to properly initialize the parent classes
        super().init()
        
        # Precompute the two moving averages
        sma1 = self.I(SMA, self.data.Close, self.n1)
        sma2 = self.I(SMA, self.data.Close, self.n2)
        
        # Where sma1 crosses sma2 upwards. Diff gives us [-1,0, *1*]
        signal = (pd.Series(sma1) > sma2).astype(int).diff().fillna(0)
        signal = signal.replace(-1, 0)  # Upwards/long only
        
        # Use 95% of available liquidity (at the time) on each order.
        # (Leaving a value of 1. would instead buy a single share.)
        entry_size = signal * .95
                
        # Set order entry sizes using the method provided by 
        # `SignalStrategy`. See the docs.
        self.set_signal(entry_size=entry_size)
        
        # Set trailing stop-loss to 2x ATR using
        # the method provided by `TrailingStrategy`
        self.set_trailing_sl(2)
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
 
    """Class for Yfinnance data retrieval"""
 
    def __init__(self,day,month,year,symbol):
        self.name = "yfin"
        self.name = "direct"
        self.day = day
        self.month = month
        self.year = year
        self.symbol = symbol
    #Download dataframe from yfinnance based on data from self
    def getDataFrame(self):
        dateObj = datetime.now()
        data = yf.download("{}".format(self.symbol), start="{}-{}-{}".format(self.year,self.day,self.month), end="{}-{}-{}".format(dateObj.year,dateObj.day,dateObj.month))
        return data
 
#class for producing Backtesting data in correct format from
#direct yahoo api request
class DirectAPI:

    def __init__(self,day,month,year,symbol):
        self.name = "direct"
        self.day = day
        self.month = month
        self.year = year
        self.symbol = symbol
    #download json object of historical data from yahoo api
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
         #read json data from yahoo querry
        data = pd.read_json("https://query1.finance.yahoo.com/v8/finance/chart/{sym}?symbol={sym}&period1={p1}&period2={p2}&interval=1d".format(sym = self.symbol,p1=period1,p2=period2))
        return data
    #convert json object to proper data frame
    def getDataFrame(self):
        data = self.apiData()
        result = pd.DataFrame()
        result['Open'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['open'])
        result['High'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['high'])
        result['Low'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['low'])
        result['Close'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['close'])
        result['Volume'] = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0]['volume'])
        return result


def handler(event, context):
  #get querry parameters
  day = event["queryStringParameters"]['day']
  month = event["queryStringParameters"]['month']
  year = event["queryStringParameters"]['year']
  funds = event["queryStringParameters"]['funds']
  strat = event["queryStringParameters"]['strategy']
  symbol = event["queryStringParameters"]['stock']
  #Adapt Classes for getting data from yahoo to objects
  objects = []
  directAPI = DirectAPI(day,month,year,symbol)
  objects.append(Adapter(directAPI,getData = directAPI.getDataFrame))
  data = objects[0].getData()


  #run the backtest
  if strat.lower() == "smacross" :
    bt = Backtest(data, SmaCross,
              cash=int(funds), commission=.002,
              exclusive_orders=True)
  if strat.lower() == "smatrailcross" :
    bt = Backtest(data, SmaTrailCross,
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