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

        t = ""
        temp = {}

        # Create a dict for each data type, add the hourly data
        for j in range(3):
            resp = requests.get(url=urls[j])
            data = resp.json()["data"]
            temp[data_type[j]] = []
            for p in data:
                temp[data_type[j]].append({"time": str(p["t"]).replace('u', '')[11:], "value": str(p["v"]).replace('u', '')})
            
        t = str(data[0]["t"]).replace('u', '').replace(' 00:00', '')
        stuff_dict[t] = temp

    pprint.pprint(stuff_dict)
    return stuff_dict


if __name__ == "__main__":
    s = "2022-04-01"
    e = "2022-04-02"
    get_stuff(s, e)