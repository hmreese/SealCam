from datetime import datetime
from datetime import timedelta

import pprint
import requests

def get_stuff(startDate, endDate):

    d1 = datetime.strptime(startDate, "%Y-%m-%d")
    d2 = datetime.strptime(endDate, "%Y-%m-%d")
    
    numdays = abs((d2 - d1).days) + 1
    
    if(numdays > 30):
        print("Too many days apart, must be 30 days or less")
        return -1

    stuff_dict = {}


    # Create a dict for each day, add dicts of each data type with their hourly data
    for i in range(numdays):
        date = (d1 + timedelta(days=i)).date()      # each day
        date = str(date).replace('-', '')           # format
        print(date)
        data_type = ["air_temperature", "air_pressure", "water_temperature"]        # data values
        urls = [" ", " ", " "]

        # Prepare urls for each data type
        for k in range(len(data_type)):
            urls[k] = "https://tidesandcurrents.noaa.gov/api/datagetter?product="+data_type[k]+"&begin_date="+date+"&end_date="+date+"&interval=h&station=9412110&time_zone=LST_LDT&units=english&format=json&application=NOS.COOPS.TAC.STATIONHOME" 


        # Create a dict for each data type, add the hourly data
        # air_temperature
        resp = requests.get(url=urls[0])
        data = resp.json()["data"]
        for d in data:
            t = str(d["t"]).replace('u', '')
            stuff_dict[t] = {"air_temperature": str(d["v"]).replace('u', '')}

        # the rest
        i = 1
        while i < len(data_type):
            resp = requests.get(url=urls[i])
            data = resp.json()["data"]
            for d in data:
                t = str(d["t"]).replace('u', '')
                stuff_dict[t][data_type[i]] = str(d["v"]).replace('u', '')
            i+=1

            # # air_pressure
            # resp = requests.get(url=urls[2])
            # data = resp.json()["data"]
            # for d in data:
            #     t = str(d["t"]).replace('u', '')
            #     stuff_dict[t]["water_temperature"] = str(d["v"]).replace('u', '')


    #pprint.pprint(stuff_dict)
    return stuff_dict

## JSON format for stuff_dict:

# stuff = {
#   'YYYY-MM-DD': {
#       'data_type1': [
#           {'time': timeval, 'value': dataval},
#           {'time': timeval, 'value': dataval}
#       ]
#       'data_type2': [
#           {'time': timeval, 'value': dataval},
#           {'time': timeval, 'value': dataval}
#       ]
#   },
#   'YYYY-MM-DD': {
#       'data_type1': [
#           {'time': timeval, 'value': dataval},
#           {'time': timeval, 'value': dataval}
#       ]
#       'data_type2': [
#           {'time': timeval, 'value': dataval},
#           {'time': timeval, 'value': dataval}
#       ]
#   }
# }

# change to for ease of csv conversion:
# stuff = {
#   'YYYY-MM-DD HH:MM': {
#       'data_type1': dataval,
#       'data_type2': dataval,
#       'data_type3': dataval
#   },
#   'YYYY-MM-DD HH:MM': {
#       'data_type1': dataval
#       'data_type2': dataval,
#       'data_type3': dataval
#   }
# }

# Date, Time, Data1, Data2, Data3

if __name__ == "__main__":
    s = "2022-04-06"
    e = "2022-04-07"
    get_stuff(s, e)