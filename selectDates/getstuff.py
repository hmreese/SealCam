from selenium import webdriver
import datetime
from selenium.webdriver.chrome.options import Options
from datetime import timedelta
from pytz import timezone

loop=1
while loop == 1:
    startDate = input("Start Date (YYYY-MM-DD): ")
    endDate = input("End Date (YYYY-MM-DD): ")
    days = int(input("How many days apart are the dates? "))
    if(days > 30):
        print("Too many days apart, must be 30 days or less")
        continue 
    readTime = input("Time (HH:MM): ")
    if(days <= 30):
        loop = 0

ct = endDate + " " + readTime

#it only has a 30 day range so the begin date needs to constantly shift
bd = startDate + " " + readTime
begin_date = bd[0:4]+bd[5:7]+bd[8:10]+'+'+bd[11:16]
end_date = ct[0:4]+ct[5:7]+ct[8:10]+'+'+ct[11:16]

#curr_time = (current_time - datetime.timedelta(minutes=30)).time()
curr_t = readTime

parse_dt = ct[:10]+" "+curr_t[:5]

forparse = parse_dt[:16]
#need to make sure minutes are a multiple of 6
minutes = int(parse_dt[14:16])
min_diff = int(parse_dt[14:16])%6

if min_diff != 0:
    forparse = parse_dt[:14]+str("{0:0=2d}".format(minutes-min_diff))
    readTimeFP = readTime[:3]+str("{0:0=2d}".format(minutes-min_diff))
    begin_date = bd[0:4]+bd[5:7]+bd[8:10]+'+'+readTimeFP
    end_date = ct[0:4]+ct[5:7]+ct[8:10]+'+'+readTimeFP

else:
    readTimeFP = readTime


options = Options()
options.headless = True
browser = webdriver.Chrome(options=options)
#air_gap, air_pressure, air_temperature, conductivity, currents, currents_survey, currents_predictions, daily_mean, datums, high_low, hourly_height, humidity, monthly_mean, one_minute_water_level, predictions, salinity, visibility, water_level, water_temperature, and wind
data_type = ["air_temperature", "air_pressure", "water_temperature"]
urls = [" ", " ", " "]

for i in range(3):
    urls[i] ="https://tidesandcurrents.noaa.gov/api/datagetter?product="+data_type[i]+"&begin_date="+begin_date+"&end_date="+end_date+"&station=9412110&time_zone=LST_LDT&units=english&format=json&application=NOS.COOPS.TAC.STATIONHOME" 


for i in range(days):
    forparse_int = int(startDate[8:])+i
    forparse = startDate[:8]+str("{0:0=2d}".format(forparse_int))+" "+readTimeFP
    print("Date and Time: ", forparse)
    for i in range(3):
        browser.get(urls[i])
        HTML = browser.page_source
        index = HTML.find(forparse);
        print_out = HTML[index:index+42]
        index = print_out.find('"v":');
        data = print_out[index+5:index+9]
        print("   ",data_type[i], data)
    print(" ")
