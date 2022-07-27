import json
import datetime
#import yfinance as yf
def handler(event, context):

  #stockInfo = yf.Ticker("GOOG")
  #dictionaryInfo = stockInfo.info
  current_time = datetime.datetime.now().time()

  body = {
      'message': 'Hello, the current time is ' + str(current_time),
      #'open': str(dictionaryInfo[0]),
      #'close': str(dictionaryInfo[1]),
      #'bid': str(dictionaryInfo[2])
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