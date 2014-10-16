#!/usr/bin/env python
# encoding: utf-8

def longestConsecutive( num):
    n= len(num)
    num.sort()
    if n<2:
        return n

    current = longest = 1
    for ix in range(1, n):
        if num[ix]-num[ix-1]==1:
            current += 1
        elif num[ix] != num[ix-1]:
            longest = max(current, longest)
            current = 1
    longest = max(current, longest)
    return longest


#num = [100, 4, 200, 1, 3,2]
num = [1,2]

print(longestConsecutive(num))
