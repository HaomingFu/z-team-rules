"""
rewrite of first missing positive number
"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A:
            return 1
        if len(A) == 1:
            return 1 if A[0] != 1 else 2
        length = len(A)
        for cursor in range(length):
            target = A[cursor]
            while 0 < target <= length and target != A[target-1]:
                new_tar = A[target-1]
                A[target-1] = target
                target = new_tar
        for cursor in range(length):
            if A[cursor] != cursor+1:
                return cursor+1
        return length+1
