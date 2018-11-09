#!/usr/bin/env python3
def reverse():
	"""This function returns the given string in reverse order"""
	string = raw_input("Please give string to reverse: ")
	reversed = string[::-1]
	return reversed

print(reverse())
