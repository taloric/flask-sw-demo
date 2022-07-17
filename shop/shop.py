import json
import time
import requests
from flask import Flask, jsonify
from skywalking import agent, config

svc_name = "py-shop-svc"

config.init(service_name=svc_name)
agent.start()

app = Flask(svc_name)

source = [{"id": "1", "name": "clothes", "price": "10"},
          {"id": "2", "name": "hats", "price": "20"},
          {"id": "3", "name": "shoes", "price": "30"},
          {"id": "4", "name": "tools", "price": "40"},
          {"id": "5", "name": "phone", "price": "50"},
          {"id": "6", "name": "battery", "price": "60"},
          {"id": "7", "name": "fans", "price": "70"}]


@app.route('/')
def shop():
    return svc_name


@app.route('/shop')
def shoplist():
    return jsonify(source)


@app.route('/shop/detail/<name>')
def shopdetail(name):
    for i in source:
        if i["name"] == name:
            return i
    return json.dumps({"result": "notfound"}), 200, {"content-type": "application/json"}


@app.route('/shop/store/detail/<name>')
def shopstore(name):
    r = requests.get('http://py-store-svc:5000/store/detail/'+name)
    return r.json()

app.run(host="0.0.0.0", debug=Flask)