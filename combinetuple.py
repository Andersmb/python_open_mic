#!/usr/bin/env python3

def totuple(a, b):
    assert len(a) == len(b), "Error: Both lists must have the same lengths!"
    return [(a[i], b[i]) for i in range(len(a))]

list1 = ["This", "is", "a", "test"]
list2 = ["And", "one", "more", "test"]

print(totuple(list1, list2))
