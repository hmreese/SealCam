from lib2to3.pgen2.token import AT
from flask import Flask, send_file
from flask_mail import Mail, Message
from flask import request
from flask import jsonify
from flask_cors import CORS
from get_stuff import *
import csv

app = Flask(__name__)
CORS(app)

# Email Setup
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'peeroverpier@gmail.com'
app.config['MAIL_PASSWORD'] = '***'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Hello World
@app.route('/', methods=['GET', 'POST'])
def helloWorld():
    if request.method == 'GET':
        return jsonify("Welcome to Seal Cam Stats!"), 200

# Home Page
@app.route('/home', methods=['GET', 'POST'])
def get_home():
    if request.method == 'GET':
        return jsonify('NOAA Data?'), 200

    elif request.method == 'POST':
        ret = request.get_json()

        # get start & end dates
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

        # for each day and time of day, write data
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

# Download CSV
@app.route('/download', methods=['GET'])
def get_csv():
    if request.method == 'GET':
        return send_file("sealcamdata.csv", as_attachment=True)

# Email CSV
@app.route('/email', methods=['POST'])
def email_csv():
    if request.method == 'POST':
        ret = request.get_json()

        try:
            email = ret["email"]
            start = ret["start"]
            end = ret["end"]
        except:
            return jsonify('Bad Request'), 400

        subject = "Seal Cam Data: {0} to {1}".format(start, end)
        msg = Message(subject, sender='peeroverpier@gmail.com', recipients=[email])
        msg.body = "Hello! Here is the seal cam data file!"
        with app.open_resource("sealcamdata.csv") as fp:
            msg.attach("sealcamdata.csv", "text/csv", fp.read())
            mail.send(msg)

        return jsonify('Email sent!'), 200

# Convert out of order json/dictionary to list of dicts
def sort_it(stuff, start):
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