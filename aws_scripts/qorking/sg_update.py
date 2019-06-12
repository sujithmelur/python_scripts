#!/usr/bin/python

import boto3
from botocore.exceptions import ClientError

available_regions=['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-3', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-north-1', 'sa-east-1', 'us-gov-east-1', 'us-gov-west-1']


sg=raw_input("Enter the SG id : ")
ip=raw_input("Enter the source IP with Subnet Mask : ")
port=input("Enter the port : ")
sr=raw_input("Mention the reason : ")

def Find_Region():

  for region in available_regions:
    try:
      ec2 = boto3.client('ec2', region)
      response = ec2.describe_security_groups(GroupIds = [sg])
      if True:
        return region
        break
    except:
      pass

reg=Find_Region()


ec2 = boto3.client('ec2',reg)
#action = ec2.authorize_security_group_ingress(GroupId=sg,IpProtocol='tcp',FromPort=port,ToPort=port,CidrIp=ip,IpPermissions=[{'FromPort':9090,'IpProtocol':'tcp','IpRanges':[{'CidrIp':'100.2.3.4/32','Description':'Test'}],'ToPort':9090}])

action = ec2.authorize_security_group_ingress(GroupId=sg,IpPermissions=[{'FromPort':port,'IpProtocol':'tcp','IpRanges':[{'CidrIp':ip,'Description':sr}],'ToPort':port}])
