from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict
import json
import datetime
import yfinance as yf
import numpy

class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy,stockName) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def getJSONData(self) -> Dict:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        #Using the given stockname, return the body of the json data
        #using the strategies method do_algorithim

        result = self._strategy.do_algorithm(self,yf.Ticker(self.stockName).info)
        return result

        # ...


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """
    #Abstract method for returning json data
    @abstractmethod
    def do_algorithm(self, data):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""

#Strategy used for filling up the react native component
#where data is the item used
class DataFormatA(Strategy):
    def do_algorithm(self, data) -> Dict:
        current_time = datetime.datetime.now().time()
        body = {
          'data': [{
          'id':"1",
          'message': 'Hello, the current time is ' + str(current_time),
          'open': str(data['open']),
          'close': str(data['previousClose']),
          'bid': str(data['bid']),
          'ask':str(data['ask']),
          'volume': str(data['volume']),
          'pegRatio': str(data['pegRatio']),
          'trailingEps': str(data['trailingEps']),
          'forwardEps': str(data['forwardEps'])
          }]
        }
        return body
#Similar strategy without ids or debug message
#any other data formats for the json data
#should be implemented as Strats
class DataFormatB(Strategy):
    def do_algorithm(self, data) -> Dict:
        body = {
          'open': str(data['open']),
          'close': str(data['previousClose']),
          'bid': str(data['bid']),
          'ask':str(data['ask']),
          'volume': str(data['volume']),
          'pegRatio': str(data['pegRatio']),
          'trailingEps': str(data['trailingEps']),
          'forwardEps': str(data['forwardEps'])
         }
        
      
        return body

class StockInformation():
  def __init__(self,stock,strat):
        self.strat = strat
        self.stock = stock
  #choose json data strategy based on parameter
  def getBody(self):
    if self.strat == "a":
      context = Context(DataFormatA,self.stock)
    else:
      context = Context(DataFormatB,self.stock)
    return context.getJSONData()
  
def handler(event, context):
  stock = event["queryStringParameters"]['stock']
  strat = event["queryStringParameters"]['strategy']
  object = StockInformation(stock,strat)
  response = {
      'statusCode': 200,
      'body': json.dumps(object.getBody()),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response
 
  