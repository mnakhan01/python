#!/usr/bin/python

def testgen(index):
	weekdays = ["sun" , "mon" , "tue" , "wed" , "thu" , "fri" , "sat"]
	yield weekdays[index]
	yield weekdays[index+2]
	yield weekdays[index+0]
day = testgen(1)
print(next(day), next(day), next(day))

