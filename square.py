#!/usr/bin/env python3

def square(l):
	return [el**2 for el in l]

mylist = [1.0, 2.0, 3.0, 4.0, 5.0, 200.0, 1/8]

print(square(mylist))
