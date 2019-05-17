from datetime import datetime
import pprint

import awsutils

instance_id = "i-0b25e4c5341c757a9"
remove_on = '20190513'

session = awsutils.get_session('us-west-1')
client = session.client('ec2')

demo = client.describe_instances()

# demo = client.describe_instances(Filters=[{'Name': 'RemoveOn',
#                                           'Values': [remove_on]}])
pprint.pprint(demo)

instance_id = demo['Reservations'][0]['Instances'][0]['InstanceId']

print(instance_id)

# stopped_instance = client.stop_instances(InstanceIds=[instance_id])

# pprint.pprint(stopped_instance)

# started_instance = client.start_instances(InstanceIds=[instance_id])
# pprint.pprint(started_instance)

'''
Alternate approach
'''
# ec2 = session.resource('ec2')
# instance = ec2.Instance(instance_id)
# print(instance.state)

# stopped_instance = instance.stop()
# pprint.pprint(stopped_instance)
# print(instance.state)

# started_instance = instance.start()
# pprint.pprint(started_instance)
# print(instance.state)

'''
Creating a backup image
'''
# date = datetime.utcnow().strftime('%Y%m%d')
#name = "InstanceID_{instance_id}_Backup_Image_{date}".format(instance_id=instance_id,
#                                                        date=date)
# ec2_image = client.create_image(InstanceId=instance_id, Name=name)
# pprint.pprint(ec2_image)

# Alternate Approach
# ec2_image = instance.create_image(Name=name + '_1')
# pprint.pprint(ec2_image)

'''
Get List of Images
'''
# images = client.describe_images(Owners=['self'])
# pprint.pprint(images)

'''
Taging ec2 instances
'''
# print(instance.tags)
# tagging instance
# ec2_tags = client.create_tags(Resources=[instance_id], Tags=[{'Key': 'RemoveOn',
#                                                              'Value': remove_on}])
# pprint.pprint(ec2_tags)


'''
Creating ec2 instance from backup image
'''
image_id = 'ami-0312992fa03073425'
ec2_instance = client.run_instances(ImageId=image_id,
                                    MinCount=1, MaxCount=1, InstanceType='t2.micro')
pprint.pprint(ec2_instance)

'''
Removing backup images
'''
# images = client.describe_images(Filters=[{'Name': 'tag:RemoveOn', 'Values': [remove_on]}])
# pprint.pprint(images)
#for img in images['Images']:
#    client.deregister_image(ImageId=img['ImageId'])

# images = client.describe_images(Filters=[{'Name': 'tag:RemoveOn', 'Values': [remove_on]}])
# pprint.pprint(images)
'''
Terminating EC2 instance
'''
# demo = client.describe_instances(Filters=[{'Name': 'tag:RemoveOn',
#                                            'Values': [remove_on]}])
# pprint.pprint(demo)
# instance_id = demo['Reservations'][0]['Instances'][0]['InstanceId']
# terminate = client.terminate_instances(InstanceIds=[instance_id])
# pprint.pprint(terminate)

