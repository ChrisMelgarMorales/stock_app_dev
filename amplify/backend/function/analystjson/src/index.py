import json
import datetime
import yfinance as yf
import numpy
def handler(event, context):
  stock = event["queryStringParameters"]['stock']
  stockInfo = yf.Ticker(stock)

  df = stockInfo.recommendations


  response = {
      'statusCode': 200,
      'body': df.to_json(orient='table'),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  return response