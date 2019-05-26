#!/usr/bin/python

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


sg = list(raw_input("enter sg id's seperated by comas : ").split(','))

for x in sg:
  response = ec2.describe_security_groups(GroupIds = [x])
  for i in response['SecurityGroups']:
    print "Security Group name is :"+i['GroupName']
    print "Security Group Id is :"+i['GroupId']
    print "Ingress Details "
    for j in i['IpPermissions']:
      for k in j['IpRanges']:
        print "IP : %s   >> Port : %s >> Protocol : %s"%(k["CidrIp"],j['FromPort'],j['IpProtocol'])
       #for k in j["IpRanges"]: 
          #print "Ingress details are Protocol : %s >> Port : %s >> IP : %s "%(j['IpProtocol',j['ToPort'],k['CidrIp'])
           #print "success"


