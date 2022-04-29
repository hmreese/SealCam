from lib2to3.pgen2.token import AT
from flask import Flask, send_file
from flask import request
from flask import jsonify
from flask_cors import CORS
from get_stuff import *
import csv
import pprint

app = Flask(__name__)
CORS(app)

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

        listofstuff = sort_it(stuff, start)

        # write to file
        f = open("sealcamdata.csv", 'w')
        writer = csv.writer(f)
        header = ["Date", "Time", "Air Temperature (F)", "Water Level (ft)", "Water Temperature (F)", "Wind Speed (kn)", "Wind Direction", "Wind Gusts (kn)"]
        writer.writerow(header)
        
        #pprint.pprint(stuff)

        for datetime in listofstuff:
            date = datetime["dt"][:10]
            time = datetime["dt"][11:]
            aTemp = datetime["air_temperature"]
            wLev = datetime["water_level"]
            wTemp = datetime["water_temperature"]
            wSpeed = datetime["wind_speed"]
            wDir = datetime["wind_dir"]
            gusts = datetime["gusts"]
            
            row = [date, time, aTemp, wLev, wTemp, wSpeed, wDir, gusts]
            writer.writerow(row)
            

        return jsonify("sealcamdata.csv now available!"), 200

# download page
@app.route('/download', methods=['GET', 'POST'])
def get_csv():
    if request.method == 'GET':
        return send_file("sealcamdata.csv", as_attachment=True)


def sort_it(stuff, start):
    # convert out of order json/dictionary to list of dicts
    l = []
    
    for dict in stuff:
        stuff[dict]["dt"] = dict      # add the datetime to the dict being added to the last
        if dict <= start:
            l.insert(stuff[dict], 0)
        else:
            l.append(stuff[dict])

    return l


if __name__ == "__main__":
  app.run()