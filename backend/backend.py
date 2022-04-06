from flask import Flask
from flask import request
from flask import jsonify
import hashlib
import json
from flask_cors import CORS
# from mongodb import User
from get_stuff import *


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

        return stuff, 200


if __name__ == "__main__":
  app.run()