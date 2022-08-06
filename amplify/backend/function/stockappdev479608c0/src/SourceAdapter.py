import json 
import pandas as pd 
from pandas.io.json import json_normalize 
from datetime import datetime

class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
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
class YFinnance:
 
    """Class for MotorCycle"""
 
    def __init__(self):
        self.name = "yfin"
 
    def TwoWheeler(self):
        return "TwoWheeler"
 
 
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
 
class Car:
 
    """Class for Car"""
 
    def __init__(self):
        self.name = "Car"
 
    def FourWheeler(self):
        return "FourWheeler"