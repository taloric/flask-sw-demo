import json
from flask import Flask, jsonify
from skywalking import agent, config

svc_name = "flask-store-svc"

config.init(service_name=svc_name)
agent.start()

app = Flask(svc_name)

source = [{"id": "1", "name": "clothes", "store": "99"},
          {"id": "2", "name": "hats", "store": "88"},
          {"id": "3", "name": "shoes", "store": "77"},
          {"id": "4", "name": "tools", "store": "66"},
          {"id": "5", "name": "phone", "store": "55"},
          {"id": "6", "name": "battery", "store": "44"},
          {"id": "7", "name": "fans", "store": "33"}]

@app.route('/')
def store():
    return svc_name

@app.route('/store')
def storelist():
    return jsonify(source)

@app.route('/store/detail/<name>')
def storedetail(name):
    for i in source:
        if i["name"] == name:
            return i
    return json.dumps({"result": "notfound"}), 200, {"content-type": "application/json"}

app.run(host="0.0.0.0", debug=Flask)