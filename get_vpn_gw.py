#!/usr/bin/python

import subprocess
import boto3
from botocore.exceptions import ClientError
import json



#ec2 = boto3.client('ec2')

available_regions=['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-3', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-north-1', 'sa-east-1', 'us-gov-east-1', 'us-gov-west-1']
resource=list(raw_input("Enter the resource name seperated by comas : ").split(','))

for x in resource:
   for region in available_regions:
     try:
       ec2 = boto3.client('ec2',region)
       #response = ec2.describe_vpn_gateways(Filters=[{'Name':'attachment.vpc-id','Values':[x],'Name':'state','Values':['available']}])
       response = ec2.describe_vpn_gateways(Filters=[{'Name':'attachment.vpc-id','Values':[x]}])
       if len(response['VpnGateways']) > 0 and (response['VpnGateways'][0]['State']=="available") :
          for i in response['VpnGateways']:
             #print "********************"
             #print "********************"
             #print "VPC Region is : %s"%region
             #for i in response['VpnGateways']:
             print "*****************************"
             print "*****************************"
             print "VPN Gateway Id is : %s"%i["VpnGatewayId"]
          break
     except:
       pass

#vpn=subprocess.Popen(['df','-h'],stdout=subprocess.PIPE)
#print a.communicate(i)
