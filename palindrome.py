#!/usr/bin/env python3
# coding=utf-8
def isthisapalindrome():
	"""This functions evalues whether a given word or phrase is a palindrome, 
	   and returns a "yes/no" answer."""

	string = input("Please give a word or phrase: ")
	s = ''.join(string.lower().split())

	# Delete special characters
	special_characters = ".,:;\"<>*^@-_!#$%&/()=?"
	
	for i,el in enumerate(special_characters):
		if el in s:
			s = ''.join(s.split(special_characters[i]))
	
	if s == s[::-1]:
		result = "Yes, your phrase '{}' is a palindrome!".format(string)
	else:
		result = "No, your phrase '{}' is not a palindrome!".format(string)
	
	return result
print(isthisapalindrome())
