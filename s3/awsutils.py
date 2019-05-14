import boto3

def get_session(region):
    return boto3.session.Session(region_name=region)

def get_bucket_list(client):
    return client.list_buckets()

