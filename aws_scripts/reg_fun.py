#!/usr/bin/python

import boto3
from botocore.exceptions import ClientError

sg = raw_input ("Enter SG id : ")

regions = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ap-northeast-2", "eu-central-1", "eu-west-1", "sa-east-1", "eu-west-2"]

def find_region(item):
   for region in regions:
     ec2 = boto3.client('ec2',region)
     try:
       response = ec2.describe_security_groups(GroupIds = sg)
       for sgs in response['SecurityGroups']:
          return  sgs['GroupName']
         
     except:
       pass


print (find_region(sg))

