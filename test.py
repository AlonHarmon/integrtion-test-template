from fixtures.helm import *
from fixtures.s3 import *

def test(install_chart, s3_client):
    assert True