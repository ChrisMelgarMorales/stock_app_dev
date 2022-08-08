import yfinance as yf
import numpy
class OriginalFrame():
    """Represents a unedited dataframe of recommendations """
 
    def __init__(self, df):
        self.df = df
 
    def getFrame(self):
        return self.df
 
class LowerBoundFrame(OriginalFrame):
    """Represent a dataframe restricted by a lower bound"""
    def __init__(self, wrapped,dateLowerBound):
        self.wrapped = wrapped
        self.dateLowerBound = dateLowerBound
 
    def getFrame(self):
        df = self.wrapped.getFrame()
        lowerbound=numpy.datetime64('now') - numpy.timedelta64(self.dateLowerBound, 'D')
        return df[(df.index >= lowerbound)]
class UpperBoundFrame(OriginalFrame):
    """Represent a dataframe restricted by a upper bound"""
    def __init__(self, wrapped,dateUpperBound):
        self.wrapped = wrapped
        self.dateUpperBound = dateUpperBound
 
    def getFrame(self):
        df = self.wrapped.getFrame()
        upperbound=numpy.datetime64('now') - numpy.timedelta64(self.dateUpperBound, 'D')
        return df[(df.index <= upperbound)]
class AnalystJSON():
  def __init__(self,stock,lower,upper):
        self.stock = stock
        self.lower = lower
        self.upper = upper
  #decorat
  def getJSON(self):
   stockInfo = yf.Ticker(self.stock)
   df = OriginalFrame(stockInfo.recommendations)
   if self.lower != "0":
      df= LowerBoundFrame(df,self.lower)
   if self.upper != "0":
      df= UpperBoundFrame(df,self.upper)
   return df.getFrame().to_json(orient='table')
def handler(event, context):
  stock = event["queryStringParameters"]['stock']
  lower = event["queryStringParameters"]['lower']
  upper = event["queryStringParameters"]['upper']
  analystJSON = AnalystJSON(stock,lower,upper)
  response = {
      'statusCode': 200,
      'body': analystJSON.getJSON(),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  return response