from func_timeout import func_timeout, FunctionTimedOut
from typing import List, Dict
import time

def wait_for_files_in_bucket(s3_client, bucket, number_of_files, timeout=120):
    def wait():
        while True:
            length = 0
            result = s3_client.list_objects_v2(Bucket=bucket)
            for _ in result['Contents']:
                length += 1

            if length >= number_of_files:
                break
            time.sleep(5)

    func_timeout(timeout, wait, args=())


def get_bucket_objects(s3_client, bucket) -> Dict[str, bytes]:
    list_objects_result = s3_client.list_objects_v2(Bucket=bucket)
    keys = [key['Key'] for key in list_objects_result['Contents']]
    objects = {}
    for key in keys:
        get_object_result = s3_client.get_object(Bucket=bucket, Key=key) 
        objects['key'] = get_object_result['Body'].read()
    return objects


def assert_objects_content(s3_client, bucket, objects_content: List[bytes]):
    objects = get_bucket_objects(s3_client, bucket)
    
    assert len(objects) == len(objects_content)

    for _, content in objects.items():
        assert content in objects_content
