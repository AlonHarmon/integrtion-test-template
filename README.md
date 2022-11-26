# integrtion-test-template
This is a template for integration / e2e test that includes support for:
  - deploying application using helm
  - pushing messages to rabbit mq
  - waiting and asserting on messages from rabbitmq
  - waiting and asserting on files written to s3


## config env vars
| name   |      description      |  deafult |
|----------|-------------|------|
| K8S_USERNAME |  k8s username | none |
| K8S_PASS |    k8s password   |   none |
| K8S_CLUSTER | cluster to deploy chart on |    none |
| HELM_CHART_REPO |    umbrella hart repo   |   none |
| ACCESS_KEY | s3 accses key |    none |
| SECRET_KEY | s3 secret key |    none |
| ENDPOINT_URL | s3 endpoint url |    none |