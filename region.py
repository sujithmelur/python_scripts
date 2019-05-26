#!/usr/bin/python

import re

available_regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-3', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-north-1', 'sa-east-1', 'us-gov-east-1', 'us-gov-west-1']

asg = raw_input("Enter the ASG : ")

for reg in available_regions:
    if re.search(reg,asg):
       region = reg

print "Region is %s"%region
