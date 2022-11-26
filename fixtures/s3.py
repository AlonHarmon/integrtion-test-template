import os
import boto3
import pytest


@pytest.fixture
def s3_configs():
    return {'aws_access_key_id': os.getenv('ACCESS_KEY'),
            'aws_secret_access_key': os.getenv('SECRET_KEY')}


@pytest.fixture
def s3_client(s3_configs):
    return boto3.client('s3', **s3_configs)
