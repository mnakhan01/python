#!/usr/bin/python

string=input("Enter a String: ")
vowels=0

for i in string:
	if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
		vowels=vowels+1
print("number of vowels: " + str(vowels))
