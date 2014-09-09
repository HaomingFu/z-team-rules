"""
From: http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
Author: Jing Zhou
Date: April 29, 2014
Thought: it's quite ugly but it works...The use of -10000 is quite arbitary
and should be avoided. I'll look for a better way to do this.
"""
def removeDuplicates(A):
    if len(A) < 2:
        return len(A)
    i = 1
    while(i < len(A)):
        if A[i] == A[i-1]:
            j = i
            while(j < len(A) and A[j]==A[i-1]):
                A[j] = -1000
                j += 1
            i = j
        i+=1
    print(A)
    i, j = 0, 0
    while(i<len(A) and A[i] != -10000):
        i += 1
    j = i
    while(i<len(A)):
        if A[i] == -10000:
            while(A[j] == -10000):
                if j==len(A)-1:
                    return i
                j += 1
            A[i] = A[j]
            A[j] = -10000
        i += 1
    return i

print(removeDuplicates([1,1,1,2,2,2,2,2,2,2,2,3,4]))
