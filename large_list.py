#!/usr/bin/python

def largest_list(items):
   max = list[0]
   for x in list:
     if x > max :
       max = x
   return max

tuple = input("enter no.s seperated by comas : ")
list = list(tuple)

print (largest_list(list))

