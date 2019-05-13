from datetime import datetime, timedelta
import awsutils
import pprint

def backup(region_id='us-west-1'):
    '''This method searches for all EC2 instances with a tag of BackUp
       and creates a backup images of them then tags the images with a
       RemoveOn tag of a YYYYMMDD value of three UTC days from now
    '''
    created_on = datetime.utcnow().strftime('%Y%m%d')
    remove_on = '20190513' # (datetime.utcnow() + timedelta(days=3)).strftime('%Y%m%d')
    session = awsutils.get_session(region_id)
    client = session.client('ec2')
    resource = session.resource('ec2')
    reservations = client.describe_instances(Filters=[{'Name': 'tag:RemoveOn',
                                                       'Values': [remove_on]}])
    # pprint.pprint(reservations)
    images = []
    for reservation in reservations['Reservations']:
        for instance_description in reservation['Instances']:
            if instance_description['State']['Name'] != 'running':
                continue
            instance_id = instance_description['InstanceId']
            name = "InstanceId_{instance_id}_RemoveOn_{remove_on}".format(instance_id=instance_id,
                                                                   remove_on=remove_on)
            print("Creating Backup: {name}".format(name=name))
            image_description = client.create_image(InstanceId=instance_id, Name=name)
            images.append(image_description['ImageId'])
            image = resource.Image(image_description['ImageId'])
            image.create_tags(Tags=[{'Key': 'RemoveOn', 'Value': remove_on},
                                    {'Key': 'Name', 'Value': name}])

if __name__ == '__main__':
    backup()
