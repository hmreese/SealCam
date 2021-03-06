from lib2to3.pgen2.token import AT
from flask import Flask, make_response, send_file
from flask import request
from flask import jsonify
#from flask_mail import Mail
import hashlib
import json
from flask_cors import CORS
# from mongodb import User
from get_stuff import *
import csv
import pprint
#import pandas
#from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)
#mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def helloWorld():
    if request.method == 'GET':
        return jsonify("Welcome to Seal Cam Stats!"), 200

# home page
@app.route('/home', methods=['GET', 'POST'])
def get_home():
    if request.method == 'GET':
        return jsonify('NOAA Data?'), 200

    elif request.method == 'POST':
        ret = request.get_json()

        try:
            start = ret["start"]
            end = ret["end"]
        except:
            return jsonify('Bad Request'), 400

        # call NOAA APIs here!
        stuff = get_stuff(start, end)
        if stuff == -1:
            return jsonify('Bad Request, Dates must be within 30 days of eachother'), 400

        # write to file
        f = open('sealcamdata.csv', 'w')
        writer = csv.writer(f)
        header = ["Date", "Time", "Air Temperature (F)", "Air Pressure (mb)", "Water Temperature (F)"]
        writer.writerow(header)
        
        #pprint.pprint(stuff)

        for datetime in stuff:
            date = datetime[:10]
            time = datetime[11:]
            aTemp = stuff[datetime]["air_temperature"]
            aPress = stuff[datetime]["air_pressure"]
            wTemp = stuff[datetime]["water_temperature"]
            
            row = [date, time, aTemp, aPress, wTemp]
            print(row)
            writer.writerow(row)
            
        #pandas.read_csv("sealcamdata.csv")

        return stuff, 200

# download page
@app.route('/download', methods=['GET', 'POST'])
def get_csv():
    if request.method == 'GET':
        # f = open('sealcamdata.csv', 'r')
        # reader = csv.reader(f)
        # csv = reader
        # response = make_response(csv)
        # cd = 'attachment; filename=sealcamdata.csv'
        # response.headers['Content-Disposition'] = cd
        # response.mimetype = 'text/csv'

        # return response
        return send_file('sealcamdata.csv', as_attachment=True)

#     if request.method == 'POST':
#         stuff = request.get_json()

#         f = open('sealcamdata.csv', 'w')
#         writer = csv.writer(f)
#         header = ["Date", "Time", "Air Temperature (F)", "Air Pressure (mb)", "Water Temperature (F)"]
#         writer.writerow(header)

#         stuff = sort_it(stuff)
        
#         for datetime in stuff:
#             date = datetime[:10]
#             time = datetime[11:]
#             aTemp = stuff[datetime]["air_temperature"]
#             aPress = stuff[datetime]["air_pressure"]
#             wTemp = stuff[datetime]["water_temperature"]
            
#             row = [date, time, aTemp, aPress, wTemp]
#             writer.writerow(row)

#         return jsonify("hello"), 200

# def sort_it(stuff):
#     # convert out of order json/dictionary to list of dicts

#     # find first date
#     date = datetime.now()
#     for dt in stuff:
#         if dt[11:] == "00:00":
#             dmy = datetime.strptime(str(dt[:10]), "%Y-%m-%d") 
#             if dmy <= date:
#                 date = dmy
    
#     ret = [{date: stuff[date]}]
#     for d in stuff:
#         if




if __name__ == "__main__":
  app.run()