#!/usr/bin/python

import subprocess
import boto3
from botocore.exceptions import ClientError
import json



available_regions=['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-3', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-north-1', 'sa-east-1', 'us-gov-east-1', 'us-gov-west-1']

resource=list(raw_input("Enter the resource name seperated by comas : ").split(','))

def Get_vgw():
   for region in available_regions:
     try:
       ec2 = boto3.client('ec2',region)
       response = ec2.describe_vpn_gateways(Filters=[{'Name':'attachment.vpc-id','Values':[x]}])
       if len(response['VpnGateways'])>0 and (response['VpnGateways'][0]['State']=="available"):
         for i in response['VpnGateways']:
           a= i["VpnGatewayId"]
           return a,region
         break
     except:
       pass

for x in resource:
  b,c=Get_vgw()
  

ec2 = boto3.client('ec2',c)
vpn_conn=ec2.describe_vpn_connections(Filters=[{'Name':'vpn-gateway-id','Values':[b]}])
if len(vpn_conn['VpnConnections'])>0:
  for n in vpn_conn['VpnConnections']:
    print "***************************************"
    print "***************************************"
    print "VPC region is %s : "%c
    print "VPN Gateway is %s : "%b
    print "VPN Connection id is : %s"%n['VpnConnectionId']
    print "Type of connection is : %s"%n['Type']
    
    for m in n['VgwTelemetry']:
      print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      print "AWS Endpoint IP is : %s"%m['OutsideIpAddress']
      print "Tunnel Status is : %s"%m['Status']
      print "Time since last status change : %s"%m['LastStatusChange']
      print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    
    print "IP's in Encryption Domain "
    
    for r in n['Routes']:

      print r['DestinationCidrBlock'],"\t\t",r['State']
        
     
  
