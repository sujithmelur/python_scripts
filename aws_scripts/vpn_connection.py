#!/usr/bin/python


import boto3
from botocore.exceptions import ClientError

#ec2 = boto3.client('ec2')

available_regions=['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-3', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-north-1', 'sa-east-1', 'us-gov-east-1', 'us-gov-west-1']
#available_regions=['us-east-2', 'us-east-1']
resource=list(raw_input("Enter the resource name seperated by comas : ").split(','))

def VPCReg():
  #for x in resource:
    for region in available_regions:
      try:
        ec2 = boto3.client('ec2',region_name = region)
        response=ec2.describe_vpcs(VpcIds = [x])
        if True:
          #return region
          print region
          break
      except:
        pass

for x in resource:
   VPCReg()
