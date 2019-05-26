#! /usr/bin/python

tuple=input("enter the nubers sep by coma : ")
list= list(tuple)

def sum_list(item):
    initial=0
    for x in list:
      initial += x
    return initial

print (sum_list(list))
