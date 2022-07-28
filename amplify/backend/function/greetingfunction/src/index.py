import json
import datetime
import yfinance as yf
import numpy
def handler(event, context):

  stockInfo = yf.Ticker("GOOG")
  dictionaryInfo = stockInfo.info
  current_time = datetime.datetime.now().time()

  body = {
      'message': 'Hello, the current time is ' + str(current_time),
      'open': str(dictionaryInfo['open']),
      'close': str(dictionaryInfo['close']),
      'bid': str(dictionaryInfo['bid']),
      'ask':str(dictionaryInfo['ask']),
      'volume': str(dictionaryInfo['volume']),
      'pegRatio': str(dictionaryInfo['pegRatio']),
      'trailingEps': str(dictionaryInfo['trailingEps']),
      'forwardEps': str(dictionaryInfo['forwardEps'])
    }

  response = {
      'statusCode': 200,
      'body': json.dumps(body),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response