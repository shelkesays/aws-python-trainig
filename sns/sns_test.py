import boto3
import awsutils
import pprint

session = awsutils.get_session("us-west-2")
client = session.client('sns')

'''
Create a topic
'''
response = client.create_topic(Name="test-topic")
pprint.pprint(response)

topic_arn = response['TopicArn']
pprint.pprint(topic_arn)

# topic_arn = 'arn:aws:sns:us-west-2:507026312405:test-topic'
'''
Create subsciprionts
'''
# client.subscribe(
#        TopicArn=topic_arn,
#        Protocol='SMS',
#        Endpoint="+12088634367"  # <-- number who'll receive an SMS message.
# )

'''
Publish to a topic
'''
# response = client.publish(
#    TopicArn=topic_arn,
#    Message='Hello World!',
#)
#pprint.pprint(response)

'''
Send SMS to phone number
'''
#response = client.publish(
#    PhoneNumber='+12088634367',
#    Message='This is test without topic!'
#)
#pprint.pprint(response)


'''
Get a list of subscriptions by topic
'''
# response = client.list_subscriptions_by_topic(TopicArn=topic_arn)
# pprint.pprint(response)

# subscriptions = [subscription for subscription in response['Subscriptions']]
# pprint.pprint(subscriptions)

'''
Get a list of subscriptions
'''
# response = client.list_subscriptions()
# subscriptions = [subscription for subscription in response['Subscriptions']]
# pprint.pprint(subscriptions)

'''
Get a list of topics
'''
# response = client.list_topics()
# pprint.pprint(response)
# topics = [topic['TopicArn'] for topic in response['Topics']]
# pprint.pprint(topics)

