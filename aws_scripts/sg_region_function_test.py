#!/usr/bin/python

import boto3
from botocore.exceptions import ClientError

#ec2 = boto3.client('ec2')

available_regions=['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-3', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-north-1', 'sa-east-1', 'us-gov-east-1', 'us-gov-west-1']
#available_regions=['us-east-2', 'us-east-1']
resource=list(raw_input("Enter the resource name seperated by comas : ").split(','))

def DesSG():
  #for x in resource:
    for region in available_regions:
      try:
        ec2 = boto3.client('ec2',region_name = region)
        response = ec2.describe_security_groups(GroupIds = [x])
	if True:
          print "**********************************************************************"
          print "**********************************************************************"
          print "Resource name is :"+x
          print "Resource region is : "+region
          for i in response['SecurityGroups']:
             print "Description :"+i['Description']
             print "Ingress Details "
             for j in i['IpPermissions']:
               for k in j['IpRanges']:
                 print "IP : %s   >> Port : %s >> Protocol : %s"%(k["CidrIp"],j['FromPort'],j['IpProtocol'])
               for m in j['UserIdGroupPairs']:
                 print "Additional SG id is %s"%m['GroupId']    
		 if m['GroupId']:
			resource.append(m['GroupId'])
	  print "---"
          break
      except:
        pass

for x in resource:
   DesSG()
