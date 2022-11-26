FROM python:buster

WORKDIR /app

# installs
## install kubectl
RUN curl -LO https://dl.k8s.io/release/v1.25.0/bin/linux/amd64/kubectl
RUN install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

## install helm
RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
RUN chmod 700 get_helm.sh
RUN ./get_helm.sh

## install pip packages
COPY requierments.txt .
RUN pip install -r requierments.txt

COPY . .

ENV K8S_USERNAME user
ENV K8S_PASS pass
ENV K8S_CLUSTER kind-kind
ENV HELM_CHART_REPO https://git.app.uib.no/caleno/helm-charts.git

CMD pytest test.py

