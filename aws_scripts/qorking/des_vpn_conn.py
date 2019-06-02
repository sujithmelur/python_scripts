#!/usr/bin/python

import subprocess
import boto3
from botocore.exceptions import ClientError
import json



#ec2 = boto3.client('ec2')

available_regions=['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-3', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-north-1', 'sa-east-1', 'us-gov-east-1', 'us-gov-west-1']
#available_regions=[ 'us-east-1']
resource=list(raw_input("Enter the resource name seperated by comas : ").split(','))

def Get_vgw():
   for region in available_regions:
     try:
       ec2 = boto3.client('ec2',region)
       response = ec2.describe_vpn_gateways(Filters=[{'Name':'attachment.vpc-id','Values':[x]}])
       if len(response['VpnGateways'])>0 and (response['VpnGateways'][0]['State']=="available"):
         for i in response['VpnGateways']:
           a= i["VpnGatewayId"]
           return a
         break
     except:
       pass

for x in resource:
  b=Get_vgw()
  #print b
  

for reg in available_regions:
  try:
    ec2 = boto3.client('ec2',reg)
    vpn_conn=ec2.describe_vpn_connections(Filters=[{'Name':'vpn-gateway-id','Values':[b]}])
    #print len(vpn_conn['VpnConnections'])
    if len(vpn_conn['VpnConnections'])>0:
      for n in vpn_conn['VpnConnections']:
        print "VPN Connection id is : %s"%n['VpnConnectionId']
        
      #print "lll"
      #print vpn_conn
      break
        # print (json.dumps(vpn_conn,sort_keys=True, indent=4))
         #print reg
         #print vpn_conn['VpnConnections']
  except:
    pass
      
  
