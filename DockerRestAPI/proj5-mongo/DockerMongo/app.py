import os
import flask
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import acp_times
#import arrow

app = Flask(__name__)
#CONFIG = config.configuration()
#app.secret_key = CONFIG.SECRET_KEY

client = MongoClient("172.19.0.2", 27017) #os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
#client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
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

#@app.route("/")
#@app.route("/index")
#def index():
#    app.logger.debug("Main page entry")
#    return flask.render_template('todo.html')

#@app.errorhandler(404)
#def page_not_found(error):
#    app.logger.debug("Page not found")
#    flask.session['linkback'] = flask.url_for("index")
#    return flask.render_template('404.html'), 404

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
    # FIXME: These probably aren't the right open and close times
    # and brevets may be longer than 200km
    open_time = acp_times.open_time(km, brevet_distance, beginning)
    close_time = acp_times.close_time(km, brevet_distance, beginning)
    rslt = {"open": open_time, "close": close_time}
    #item_doc = {
    #    'open': open_time, #request.form['open'],
    #    'close': close_time #request.form['close']
    #}
    #app.logger.debug(open_time) #request.form['open'])
    #app.logger.debug(close_time) #request.form['close'])
    #db.tododb.insert_one(item_doc)
    return flask.jsonify(result=rslt)

@app.route('/submit', methods=['POST'])
def new():
    #app.logger.debug("request.form: "+str(request.form))
    #app.logger.debug(request.form)
    openTimes = []
    closeTimes = []
    for i in request.form.getlist("open"):
        #app.logger.debug(i)
        if i != "":
            openTimes.append(i)
            #app.logger.debug(i)
    for i in request.form.getlist("close"):
        if i != "":
            closeTimes.append(i)
            #app.loo gger.debug(i)
    if (len(openTimes)==0):
        return render_template('emptyEntries.html')
    for i in range(len(openTimes)):
        item_open = {
            'open': openTimes[i],
        }
        item_close = {'close': closeTimes[i]}
        #app.logger.debug("Value openTimes: "+openTimes[i]+"Value closeTimes: "+closeTimes[i])
        #app.logger.debug(item_doc)
        db.tododb.insert_one(item_close)
        db.tododb.insert_one(item_open)


    return render_template('calc.html') #redirect(url_for('calc'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
