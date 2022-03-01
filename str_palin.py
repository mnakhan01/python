#!/usr/bin/python

string=input("Enter String: ")
if (string == string[::-1]):
	print("The String is a palindrome")
else:
	print("The String is not a palindrome")
