import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups()
    for i in response["SecurityGroups"]:
      print(i["GroupId"])
except ClientError as e:
    print(e)
