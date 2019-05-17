import boto3
import pprint
import json
import awsutils


session = awsutils.get_session("us-west-1")
client = session.client('cloudwatch')

region = "us-west-1"
ec2_instance_id = "i-0ce24ed4cc2535075"
user_account_id = 507026312405
'''
Create a Dashboard
'''
"""
dashboard_body = {
   "start": "-PT6H",
   "periodOverride": "inherit",
   "widgets": [
      {
         "type":"metric",
         "x":0,
         "y":0,
         "width":12,
         "height":6,
         "properties":{
            "metrics":[
               [
                  "AWS/EC2",
                  "CPUUtilization",
                  "InstanceId",
                  ec2_instance_id,
               ]
            ],
            "period":300,
            "stat":"Average",
            "region":region,
            "title":"EC2 Instance CPU Utilization"
         }
      }
   ]
}
json_body = json.dumps(dashboard_body)

response = client.put_dashboard(
    DashboardName="aws_training_test",
    DashboardBody=json_body
)
pprint.pprint(response)

"""

'''
Create Alarm
'''
"""
response = client.put_metric_alarm(
    AlarmName="Web_Server_CPU_Utilization_{0}".format(ec2_instance_id),
    AlarmDescription='Alarm when server CPU exceeds 70%',
    ActionsEnabled=False,
    MetricName="CPUUtilization",
    Namespace="AWS/EC2",
    Statistic='Average',
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': ec2_instance_id  # <== Put instance id here
        },
    ],
    Period=300,
    Unit='Seconds',
    EvaluationPeriods=1,
    Threshold=0.5,
    ComparisonOperator='GreaterThanThreshold',
)

pprint.pprint(response)
"""

'''
Disable actions
'''
# client.disable_alarm_actions(AlarmNames=['Web_Server_CPU_Utilization_{0}'.format(ec2_instance_id)])

'''
Delete an alarm
'''
# client.delete_alarms(AlarmNames=['Web_Server_CPU_Utilization_{0}'.format(ec2_instance_id)])

'''
Publish a custom metrics
'''
"""
response = client.put_metric_data(
    MetricData=[
        {
            'MetricName': 'PAGES_VISITED',
            'Dimensions': [
                {
                    'Name': 'UNIQUE_PAGES',
                    'Value': 'https://aws.amazon.com/cloudwatch'
                },
            ],
            'Unit': 'None',
            'Value': 1.0
        },
    ],
    Namespace='SITE/TRAFFIC'
)
pprint.pprint(response)
"""

'''
List Metric Names
'''

#response = client.list_metrics(
#     Namespace = 'SITE/TRAFFIC',
#     MetricName = 'PAGES_VISITED'
#)
#pprint.pprint(response)
#paginator = client.get_paginator('list_metrics')
#for response in paginator.paginate(Dimensions=[{'Name': 'UNIQUE_PAGES'}],
#                                   MetricName='PAGES_VISITED',
#                                   Namespace='SITE/TRAFFIC'):
#    pprint.pprint(response['Metrics'])

'''
List all cloudwatch alarms
'''
#paginator = client.get_paginator('describe_alarms')
#for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
#    pprint.pprint(response['MetricAlarms'])
