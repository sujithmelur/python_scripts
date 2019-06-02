#!/usr/bin/python

import boto3
from botocore.exceptions import ClientError

#ec2 = boto3.client('ec2')

available_regions=['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-3', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-north-1', 'sa-east-1', 'us-gov-east-1', 'us-gov-west-1']

resource=list(raw_input("Enter the resource name seperated by comas : ").split(','))


def find_region():
  #global region
  for x  in resource:
  #print x
    for region in available_regions:
       ec2 = boto3.client('ec2',region_name = region)
       try:
         #print region
         response = ec2.describe_security_groups(GroupIds = [x])
         if True:
	   return region
           #break
       except:
         pass


print find_region()
