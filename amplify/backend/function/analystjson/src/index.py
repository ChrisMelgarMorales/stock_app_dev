import json
import datetime
import yfinance as yf
import numpy
def handler(event, context):
  stock = event["queryStringParameters"]['stock']
  stockInfo = yf.Ticker(stock)

  df = stockInfo.analyst(orient="index")


  response = {
      'statusCode': 200,
      'body': df.to_json(),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  return response