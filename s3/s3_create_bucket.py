import uuid
import pprint
import awsutils

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, client, region):
    bucket_name = create_bucket_name(bucket_prefix)
    # print(bucket_name)
    bucket_response = client.create_bucket(Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region})
    return bucket_name, bucket_response


if __name__ == "__main__":
    region = "us-west-1"
    bucket_prefix = "aws-python-training-"
    session = awsutils.get_session(region)
    client = session.client('s3')
    bucket_name, bucket_response = create_bucket(bucket_prefix, client, region)
    print(bucket_name)
    pprint.pprint(bucket_response)
