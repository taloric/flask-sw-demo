import json
import time
import threading
import requests
from flask import Flask, jsonify
from skywalking import agent, config
from skywalking import Component
from skywalking.decorators import trace, runnable
from skywalking.trace.context import SpanContext, get_context
context: SpanContext = get_context()

svc_name = "flask-app-svc"

config.init(service_name=svc_name)
agent.start()

app = Flask(svc_name)

source = ["clothes", "hats", "shoes", "tools", "phone", "battery", "fans"]


@app.route('/')
def ui():
    return svc_name


@app.route('/app/shop')
def appshop():
    r = requests.get('http://flask-shop-svc:5000/shop')
    result = r.json()
    return jsonify(result)


@app.route('/app/shop/<name>')
def appshopname(name):
    r = requests.get('http://flask-shop-svc:5000/shop/detail/'+name)
    result = r.json()
    return jsonify(result)


@app.route('/app/store')
def appstore():
    r = requests.get('http://flask-store-svc:5000/store')
    result = r.json()
    return jsonify(result)


@app.route('/app/store/<name>')
def appstorename(name):
    r = requests.get('http://flask-store-svc:5000/store/detail/'+name)
    result = r.json()
    return jsonify(result)


@runnable()
def getshopdetail(i: str):
    print("start threading getshopdetail")
    requests.get('http://flask-shop-svc:5000/shop/detail/'+i)


@runnable()
def getstoredetail(i: str):
    print("start threading getstoredetail")
    requests.get('http://flask-store-svc:5000/store/detail/'+i)


@runnable()
def getshopstoredetail(i: str):
    print("start threading getshopstoredetail")
    requests.get('http://flask-shop-svc:5000/shop/store/detail/'+i)
    t1 = threading.Thread(target=getshopdetail, args=[i])
    t1.start()
    t2 = threading.Thread(target=getstoredetail, args=[i])
    t2.start()
    t1.join()
    t2.join()


@app.route('/app/testall')
def appfulltest():
    context.put_correlation('correlation', 'correlation')
    with context.new_entry_span(op=str('cross thread')) as span:
        span.component = Component.Flask

        requests.get('http://flask-shop-svc:5000/shop')
        requests.get('http://flask-store-svc:5000/store')
        for i in source:
            t3 = threading.Thread(target=getshopstoredetail, args=[i])
            t3.start()
            t3.join()

    return json.dumps({"result": "ok"}), 200, {"content-type": "application/json"}


app.run(host="0.0.0.0", debug=Flask)
