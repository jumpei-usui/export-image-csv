import os
import json
import boto3


def handler(event, context):
    bucket_name = os.environ.get("BUCKET_NAME")

    s3_client = boto3.client("s3")
    response = s3_client.list_objects_v2(Bucket=bucket_name, MaxKeys=100)

    object_keys = [obj["Key"] for obj in response["Contents"]]

    return object_keys
