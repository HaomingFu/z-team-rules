"""
From: http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
Author: Jing Zhou
Date: April 29, 2014
Thought: HAHAHAHAHA this one i smuch simpler...
and should be avoided. I'll look for a better way to do this.
"""
def removeDuplicates(A):
    if len(A) < 2:
        return len(A)
    i,j = 0, 1
    while(j < len(A)):
        if A[j] != A[i]:
            i += 1
            A[i] = A[j]
        j += 1
    print(A)
    return i+1

print(removeDuplicates([1,1,1,2,2,2,2,2,2,2,2,3,4]))
