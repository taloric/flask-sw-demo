PROJECT=ui store shop

.PHONY: app
app: 
	$(foreach ap, $(PROJECT), echo ${ap}; cd ${ap}; docker build -t taloricag/flask-sw-demo-${ap}:latest . ; cd .. ;)

.PHONY: load
load: 
	cd loadgenerator && docker build -t taloricag/flask-sw-demo-loadgenerator:0.1.0 .

build: load app