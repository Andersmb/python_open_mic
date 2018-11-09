#!/usr/bin/env python3
# coding=utf-8
def isthisanisogram():
	string = raw_input("Please give a word or phrase: ").lower()
	nospace = ''.join(string.split())
	characters = "abcdefghijklmnopqrstuvwxyzæøå"
	

	val = 0
	for i in characters:
		if i in nospace:
			val += 1
			
	if val == len(nospace):
		result = "Your phrase '{}' is an isogram!".format(string)
	else:
		result = "Your phrase '{}' is not an isogram!".format(string)
	
	return result

print(isthisanisogram())
