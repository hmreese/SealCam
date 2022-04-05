from selenium import webdriver
import datetime
from selenium.webdriver.chrome.options import Options
from datetime import timedelta
from pytz import timezone
from datetime import datetime

import pprint
import requests
import json

def get_stuff(startDate, endDate):
    # loop=1
    # while loop == 1:
        #startDate = input("Start Date (YYYY-MM-DD): ")
        #endDate = input("End Date (YYYY-MM-DD): ")
        #days = int(input("How many days apart are the dates? "))
    d1 = datetime.strptime(startDate, "%Y-%m-%d")
    d2 = datetime.strptime(endDate, "%Y-%m-%d")
    days = abs((d2 - d1).days)
    if(days > 30):
        print("Too many days apart, must be 30 days or less")
        return -1
        #readTime = input("Time (HH:MM): ")
        # if(days <= 30):
        #     loop = 0

    # s = "00:00"
    # e = "23:00"
    # ct = endDate + " " + e

    #it only has a 30 day range so the begin date needs to constantly shift
    #bd = startDate + " " + s
    # begin_date = bd[0:4]+bd[5:7]+bd[8:10] #+'+'+bd[11:16]
    # end_date = ct[0:4]+ct[5:7]+ct[8:10]   #+'+'+ct[11:16]
    begin_date = startDate.replace('-', '')
    end_date = startDate.replace('-', '')

    #curr_time = (current_time - datetime.timedelta(minutes=30)).time()
    # curr_t = s

    # parse_dt = ct[:10] + " " + curr_t[:5]

    # forparse = parse_dt[:16]
    #need to make sure minutes are a multiple of 6
    # minutes = int(parse_dt[14:16])
    # min_diff = int(parse_dt[14:16])%6

    # if min_diff != 0:
    #     forparse = parse_dt[:14]+str("{0:0=2d}".format(minutes-min_diff))
    #     readTimeFP = readTime[:3]+str("{0:0=2d}".format(minutes-min_diff))
    #     begin_date = bd[0:4]+bd[5:7]+bd[8:10]+'+'+readTimeFP
    #     end_date = ct[0:4]+ct[5:7]+ct[8:10]+'+'+readTimeFP

    # else:
    #     readTimeFP = readTime


    # options = Options()
    # options.headless = True
    # path = "/Users/hannahreese/Downloads/chromedriver"
    # browser = webdriver.Chrome(options=options, executable_path=path)
    #air_gap, air_pressure, air_temperature, conductivity, currents, currents_survey, currents_predictions, daily_mean, datums, high_low, hourly_height, humidity, monthly_mean, one_minute_water_level, predictions, salinity, visibility, water_level, water_temperature, and wind
    data_type = ["air_temperature", "air_pressure", "water_temperature"]
    urls = [" ", " ", " "]

    times = ["00:00", "01:00", "02:00", ]

    for i in range(3):
        urls[i] = "https://tidesandcurrents.noaa.gov/api/datagetter?product="+data_type[i]+"&begin_date="+begin_date+"&end_date="+end_date+"&interval=h&station=9412110&time_zone=LST_LDT&units=english&format=json&application=NOS.COOPS.TAC.STATIONHOME" 

    stuff_dict = {}

    # Create a dict for each day, add dicts of each data type with their hourly data
    for i in range(days + 1):
        day = int(begin_date) + i
        print("Date: {0}".format(day))
        t = ""
        temp = {}

        # Create a dict for each data type, add the hourly data
        for j in range(3):
            resp = requests.get(url=urls[j])
            data = resp.json()["data"]
            temp[data_type[j]] = []
            for p in data:
                temp[data_type[j]].append({"t": str(p["t"]).replace('u', '')[11:], "v": str(p["v"]).replace('u', '')})
            
        t = str(data[0]["t"]).replace('u', '').replace(' 00:00', '')
        stuff_dict[t] = temp

    pprint.pprint(stuff_dict)

    # for i in range(days + 1):
    #     forparse_int = int(startDate[8:])+i
    #     forparse = startDate[:8]+str("{0:0=2d}".format(forparse_int)) #+" "+readTimeFP
    #     print("Date and Time: ", forparse)
    #     for j in range(3):
    #         for k in times:
    #             dtime = forparse + " " + k
    #             browser.get(urls[j])
    #             HTML = browser.page_source
    #             index = HTML.find(dtime)
    #             print_out = HTML[index:index+42]
    #             index = print_out.find('"v":')
    #             data = print_out[index+5:index+9]
    #             print("   ",data_type[j], data)
    #     print(" ")

    # browser.quit()

if __name__ == "__main__":
    s = "2022-04-01"
    e = "2022-04-02"
    get_stuff(s, e)