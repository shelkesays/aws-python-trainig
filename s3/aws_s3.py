import awsutils
import pprint

session = awsutils.get_session("us-west-1")
client = session.client('s3')

# resource = session.resource('s3')
'''
Get a list of buckets
'''
# bucket_list = client.list_buckets()

# pprint.pprint(bucket_list)

'''
Get all bucket names
'''
# for bucket in bucket_list['Buckets']:
#    print(bucket['Name'])

# bucket_name = bucket_list['Buckets'][0]['Name']
'''
Upload file / object
'''
# with open("s3_trial.png", "r+b") as file:
#    client.upload_fileobj(file, bucket_name, 'boto3_file.png')

'''
Download file / object
'''
# with open('aws_training.png', "w+b") as file:
#    client.download_fileobj(bucket_name, 'boto3_file.png', file)

'''
Connecting to a bucket
'''
# bucket = resource.Bucket(bucket_name)
# pprint.pprint(bucket)
'''
Get list of all the files
'''
# for object in bucket.objects.all():
#    pprint.pprint(object)
'''
Creating bucket
'''
# client.create_bucket(Bucket="new-bucket-20190514-123456789",
#                     CreateBucketConfiguration={'LocationConstraint': 'us-west-1'})
# pprint.pprint(awsutils.get_bucket_list(client))
