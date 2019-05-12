from datetime import datetime, timedelta
import awsutils

def backup(region_id='us-west-1'):
    '''This method searches for all EC2 instances with a tag of BackUp
       and creates a backup images of them then tags the images with a
       RemoveOn tag of a YYYYMMDD value of three UTC days from now
    '''
    created_on = datetime.utcnow().strftime('%Y%m%d')
    remove_on = (datetime.utcnow() + timedelta(days=3)).strftime('%Y%m%d')
    session = awsutils.get_session(region_id)
    client = session.client('ec2')
    resource = session.resource('ec2')
    reservations = client.describe_instances(Filters=[{'Name': 'tag-key', 'Values': ['BackUp']}])
    images = []
    for reservation in reservations['Reservations']:
        for instance_description in reservation['Instances']:
            instance_id = instance_description['InstanceId']
            name = "InstanceId({instance_id})_CreatedOn({created_on})_RemoveOn({remove_on})"
            print("Creating Backup: {name}")
            image_description = client.create_image(InstanceId=instance_id, Name=name)
            images.append(image_description['ImageId'])
            image = resource.Image(image_description['ImageId'])
            image.create_tags(Tags=[{'Key': 'RemoveOn', 'Value': remove_on},
                                    {'Key': 'Name', 'Value': name}])

if __name__ == '__main__':
    backup()
