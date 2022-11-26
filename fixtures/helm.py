import pytest
import subprocess
import os


@pytest.fixture
def deployment_config():
    return {'<put here youre integration test configs>': 'bar'}


@pytest.fixture
def cluster_creds():
    return {'username': os.getenv('K8S_USERNAME'),
            'password': os.getenv('K8S_PASS'),
            'cluster': os.getenv('K8S_CLUSTER')}


@pytest.fixture
def chart():
    return os.getenv('HELM_CHART_REPO')


@pytest.fixture
def login_to_cluster(cluster_creds):
    subprocess.run(['kubectl', 'config', 'set-credentials', cluster_creds['cluster'],
     '--username',  cluster_creds['username'],
     '--password', cluster_creds['password']])


@pytest.fixture
def install_chart(login_to_cluster, chart, deployment_config):
    subprocess.run(['helm', 'install', 'integration-test-release', chart])
    yield deployment_config
    subprocess.run(['helm', 'uninstall', 'integration-test-release'])
