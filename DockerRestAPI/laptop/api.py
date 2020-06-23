# Laptop Service

import os
from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson.json_util import loads, dumps
import json
import pandas


# Instantiate the app
app = Flask(__name__)
api = Api(app)

#client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
client = MongoClient("172.19.0.2", 27017)
db = client.tododb
col = db.tododb

#enterThis = { 'Tips':['The','Juice','also juiced'] }
#enterThis2 = { 'TipsTops':['The','Juice','also juiced'] }
#db.tododb.insert_one(enterThis)
#db.tododb.insert_one(enterThis2)

def myClose(e):
    return e['close']

def myOpen(e):
    return e['open']


class Instructions(Resource):
    def get(self):
        return {
            'Laptops': ['Mac OS', 'Dell', 
            'Windozzee',
	    'Yet another laptop!',
	    'Yet yet another laptop!'
            ]
        }

"""Getting the default formats"""
class AllTimes(Resource):
    def get(self):
        return json.loads(dumps(db.tododb.find()))

class OpenTimes(Resource):
    def get(self):
        ret = []
        for i in json.loads(dumps(db.tododb.find({}, {"open":1}))):
            if len(i) != 1:
                app.logger.debug(i)
                ret.append(i)

        retOpen = json.loads(dumps(ret)) 
        return retOpen 

class CloseTimes(Resource):
    def get(self):
        ret = []
        for i in json.loads(dumps(db.tododb.find({}, {"close":1}))):
            if len(i) != 1:
                app.logger.debug(i)
                ret.append(i)

        return json.loads(dumps(ret))

"""Getting the JSON formats"""
class AllTimesJSON(Resource):
    def get(self):
        return json.loads(dumps(db.tododb.find()))

class OpenTimesJSON(Resource):
    def get(self):
        ret = []
        topK = request.args.get("top")
        app.logger.debug(topK)
        for i in json.loads(dumps(db.tododb.find({}, {"open":1}))):
            if len(i) != 1:
                if '_id' in i:
                    del i['_id']
                app.logger.debug(i)
                ret.append(i)
                ret.sort(key=myOpen)
        if topK != None:
            cnt = 0
            topKList = []
            for i in ret:
                app.logger.debug(i)
                if '_id' in i:
                    del i['_id']
                if len(i) != 0:
                    cnt += 1
                    topKList.append(i)
                    if cnt == int(topK):
                        return topKList

        return json.loads(dumps(ret)) 




class CloseTimesJSON(Resource):
    def get(self):
        ret = []
        topK = request.args.get("top")
        app.logger.debug(topK)
        for i in json.loads(dumps(db.tododb.find({}, {"close":1}))):
            if len(i) != 1:
                if '_id' in i:
                    del i['_id']
                app.logger.debug(i)
                ret.append(i)
                ret.sort(key=myClose)
        if topK != None:
            cnt = 0
            topKList = []
            for i in ret:
                app.logger.debug(i)
                if '_id' in i:
                    del i['_id']
                if len(i) != 0:
                    cnt += 1
                    topKList.append(i)
                    if cnt == int(topK):
                        return topKList
        return json.loads(dumps(ret))


"""Getting the CSV formats"""
class AllTimesCSV(Resource):
    def get(self):
        data = db.tododb.find()
        df = pandas.DataFrame(json.loads(dumps(data)))
        return df.to_csv()

class OpenTimesCSV(Resource):
    def get(self):
        ret = []
        topK = request.args.get("top")
        app.logger.debug(topK)
        for i in json.loads(dumps(db.tododb.find({}, {"open":1}))):
            if len(i) != 1:
                if '_id' in i:
                    del i['_id']
                app.logger.debug(i)
                ret.append(i)
                ret.sort(key=myOpen)
        if topK != None:
            cnt = 0
            topKList = []
            for i in ret:
                app.logger.debug(i)
                if '_id' in i:
                    del i['_id']
                if len(i) != 0:
                    cnt += 1
                    topKList.append(i)
                    
                    if cnt == int(topK):
                        return pandas.DataFrame(json.loads(dumps(topKList))).to_csv()

        return pandas.DataFrame(json.loads(dumps(ret))).to_csv() 
            
class CloseTimesCSV(Resource):
    def get(self):
        ret = []
        topK = request.args.get("top")
        app.logger.debug(topK)
        for i in json.loads(dumps(db.tododb.find({}, {"close":1}))):
            if len(i) != 1:
                if '_id' in i:
                    del i['_id']
                app.logger.debug(i)
                ret.append(i)
                ret.sort(key=myClose)
        if topK != None:
            cnt = 0
            topKList = []
            for i in ret:
                app.logger.debug(i)
                if '_id' in i:
                    del i['_id']
                if len(i) != 0:
                    cnt += 1
                    topKList.append(i)
                    if cnt == int(topK):
                        return pandas.DataFrame(json.loads(dumps(topKList))).to_csv()

        return pandas.DataFrame(json.loads(dumps(ret))).to_csv()



# Create routes
# Another way, without decorators
#api.add_resource(Laptops, '/')
api.add_resource(Instructions, '/')
api.add_resource(AllTimes, '/listAll')
api.add_resource(OpenTimes, '/listOpenOnly')
api.add_resource(CloseTimes, '/listCloseOnly')
api.add_resource(AllTimesJSON, '/listAll/json')
api.add_resource(OpenTimesJSON, '/listOpenOnly/json')
api.add_resource(CloseTimesJSON, '/listCloseOnly/json')
api.add_resource(AllTimesCSV, '/listAll/csv')
api.add_resource(OpenTimesCSV, '/listOpenOnly/csv')
api.add_resource(CloseTimesCSV, '/listCloseOnly/csv')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
