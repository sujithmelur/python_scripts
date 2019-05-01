#!/usr/bin/python

import os
target = "/etc/redhat-release"
file = open(target,'r')
release=file.read()

print (release)
