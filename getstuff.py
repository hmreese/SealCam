from selenium import webdriver
import datetime
from datetime import timedelta
from pytz import timezone

current_time = datetime.datetime.now(timezone('US/Pacific'))
ct = str(current_time)

#it only has a 30 day range so the begin date needs to constantly shift
bt = current_time - datetime.timedelta(days=30)
bd = str(bt)
begin_date = bd[0:4]+bd[5:7]+bd[8:10]+'+'+bd[11:16]
end_date = ct[0:4]+ct[5:7]+ct[8:10]+'+'+ct[11:16]

curr_time = (current_time - datetime.timedelta(minutes=30)).time()

curr_t = str(curr_time)
parse_dt = ct[:10]+" "+curr_t[:5]

forparse = parse_dt[:16]
#need to make sure minutes are a multiple of 6
minutes = int(parse_dt[14:16])
min_diff = int(parse_dt[14:16])%6

if min_diff != 0:
    forparse = parse_dt[:14]+str("{0:0=2d}".format(minutes-min_diff))

browser = webdriver.Chrome()

data_type = ["air_temperature", "air_pressure", "water_temperature"]
urls = [" ", " ", " "]

for i in range(3):
    urls[i] ="https://tidesandcurrents.noaa.gov/api/datagetter?product="+data_type[i]+"&begin_date="+begin_date+"&end_date="+end_date+"&station=9412110&time_zone=LST_LDT&units=english&format=json&application=NOS.COOPS.TAC.STATIONHOME" 


print("Date and Time: ", forparse)
for i in range(3):
    browser.get(urls[i])
    HTML = browser.page_source
    index = HTML.find(forparse);
    #index = HTML.find("2022-02-16 14:06");
    print_out = HTML[index:index+42]
    index = print_out.find('"v":');
    data = print_out[index+5:index+9]
    print(data_type[i], data)

