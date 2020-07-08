import os
import flask
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import acp_times
#import arrow

app = Flask(__name__)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017) # If this line returns a KeyError, run docker inspect <mongo-container-id>,
                                                                  # then find the ip address within the json that is returned, and use that.
                                                                  # The next line is an example of this.
#client = MongoClient('IP-address-that-was-found-in-json', 27017)

db = client.tododb

@app.route('/')
def showPage():
    return render_template('calc.html')

@app.route('/render_calc')
def render_calc():
    return render_template('calc.html')

@app.route('/todo', methods=["GET", "POST"])
def todo():
    app.logger.debug("The Juice!")
    _items = db.tododb.find()
    items = [item for item in _items]
    if len(items) > 0:
        return render_template('todo.html', items=items)
    else:
        return render_template('noEntries.html')

@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    brevet_distance = request.args.get('brevet_distance', type=int)
    beginTime = request.args.get('begin_time', type=str)
    beginDate = request.args.get('begin_date', type=str)
    beginning = beginDate.format('MM-DD-YYYY') +" "+ beginTime.format('HH:mm')
    app.logger.debug("beginTime={}".format(beginTime))
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    open_time = acp_times.open_time(km, brevet_distance, beginning)
    close_time = acp_times.close_time(km, brevet_distance, beginning)
    rslt = {"open": open_time, "close": close_time}

    return flask.jsonify(result=rslt)

@app.route('/submit', methods=['POST'])
def new():
    openTimes = []
    closeTimes = []
    for i in request.form.getlist("open"):
        if i != "":
            openTimes.append(i)
    for i in request.form.getlist("close"):
        if i != "":
            closeTimes.append(i)
    if (len(openTimes)==0):
        return render_template('emptyEntries.html')
    for i in range(len(openTimes)):
        item_open = {
            'open': openTimes[i],
        }
        item_close = {'close': closeTimes[i]}
        db.tododb.insert_one(item_close)
        db.tododb.insert_one(item_open)


    return render_template('calc.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
