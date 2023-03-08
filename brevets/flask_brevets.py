"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
#from mypymongo import brevet_insert, brevet_find
import os
import requests

###
# Globals
###
app = flask.Flask(__name__)
app.debug = True if "DEBUG" not in os.environ else os.environ["DEBUG"]
port_num = True if "PORT" not in os.environ else os.environ["PORT"]

###
# Pages
###

API_ADDR = os.environ["API_ADDR"]
API_PORT = os.environ["API_PORT"]
API_URL = f"http://{API_ADDR}:{API_PORT}/api/"

def brevet_find():
    """
    Obtains the newest document in the "lists" collection in database
    by calling the RESTful API.

    Returns title (string) and items (list of dictionaries) as a tuple.
    """
    # Get documents (rows) in our collection (table),
    # Sort by primary key in descending order and limit to 1 document (row)
    # This will translate into finding the newest inserted document.

    brevets = requests.get(f"{API_URL}/brevets").json()

    # lists should be a list of dictionaries.
    # we just need the last one:
    brevet = brevets[-1]
    return brevet["brevet_dist_km"], brevet["begin_date"], brevet["items"]


def brevet_insert(brevet_dist_km, begin_date, items):
    """
    Inserts a new to-do list into the database by calling the API.
    
    Inputs a title (string) and items (list of dictionaries)
    """
    _id = requests.post(f"{API_URL}/brevets", json={"brevet_dist_km": brevet_dist_km, "begin_date": begin_date, "items": items}).json()
    return _id

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    app.logger.debug("km={}".format(km))

    brevet_dist_km = request.args.get("brevet_dist_km", type=float)
    app.logger.debug("brevet_dist_km={}".format(brevet_dist_km))

    start_time = request.args.get("begin_date", type=str)
    start_time = arrow.get(start_time, "YYYY-MM-DDTHH:mm")

    app.logger.debug("start_time={}".format(start_time))

    app.logger.debug("request.args: {}".format(request.args))

    # FIXME!
    # Right now, only the current time is passed as the start time
    # and control distance is fixed to 200
    # You should get these from the webpage!
    open_time = acp_times.open_time(km, brevet_dist_km, start_time).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, brevet_dist_km, start_time).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)

@app.route("/insert", methods=["POST"])
def insert():
    try:
        input_json = request.json
        brevet_dist_km = input_json["brevet_dist_km"] # Should be a string
        begin_date = input_json["begin_date"] # Should be a string
        items = input_json["items"] # Should be a list of dictionaries

        brevet_id = brevet_insert(brevet_dist_km, begin_date, items)

        return flask.jsonify(result={},
                        message="Inserted!", 
                        status=1,
                        mongo_id=brevet_id)
    except:
        return flask.jsonify(result={},
                        message="Oh no! Server error!", 
                        status=0, 
                        mongo_id='None')
@app.route("/fetch")
def fetch():
    try:
        brevet_dist_km, begin_date, items = brevet_find()
        return flask.jsonify(
                result={"brevet_dist_km": brevet_dist_km, "begin_date": begin_date, "items": items}, 
                status=1,
                message="Successfully fetched a brevet list!")
    except:
        return flask.jsonify(
                result={}, 
                status=0,
                message="Something went wrong, couldn't fetch any lists!")

#############

app.debug = os.environ["DEBUG"]

if __name__ == "__main__":
    app.run(port=os.environ["PORT"], host="0.0.0.0")
