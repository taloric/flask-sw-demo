### Python Microservice Demo 

#### Web Framework flask

- Feature: 
  - using [skywalking python auto instrument](https://github.com/apache/skywalking-python)
  - using [OpenTelemetry](https://opentelemetry.io/) and [Jaeger](https://www.jaegertracing.io/) to see trace results.

#### Quick Start

```bash
git clone https://github.com/taloric/flask-sw-demo

kubectl apply -f flask-sw-demo/k8s-deployment.yaml
```

#### Requirements

- Kubernetes / minikube / k3s ....
- [Otel](https://opentelemetry.io/docs/collector/deployment/) deploys in cluster
