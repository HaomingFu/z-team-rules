"""
From:   http://oj.leetcode.com/problems/search-a-2d-matrix/
Author: Jing Zhou
Date: May 15, 2014
Thought: I'm still having trouble with binary search... CRAP!!!
I have three different ideas in mind. Two of them worked. Will try the third.
the quickest one should be log(m)+log(n)... the one here is m*n... not so good...
"""


def searchMatrix(matrix, target):
    if not matrix:
        return False
    merged = [item for sublist in matrix for item in sublist]
    """
    Alteratively:
    if target in matrix:
        return True
    return False
    """
    if target < merged[0] or target > merged[-1]:
        return False
    return search(merged,0, len(merged)-1, target)
def search(l, left, right, target):
    if left == right and l[left] != target:
        return False
    mid = (left+right)/2
    if mid > right or mid < left:
        return False
    if target > l[mid]:
        return search(l, mid+1, right, target)
    elif target < l[mid]:
        return search(l, left, mid, target)
    elif target == l[mid]:
        return True
    else:
        return False

def test():
    print(searchMatrix([[1, 3]], 2))
test()
