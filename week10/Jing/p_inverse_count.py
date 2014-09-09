"""
From: https://class.coursera.org/algo-005/quiz/start?quiz_id=31
Author: Jing Zhou
Date: May 18, 2014
Thought: This one is O(nlg(n)), the idea of mergesort
"""


def mergeSortCount(l, left, right, copy):
    if left >= right:
        return 0
    mid = (left+right)//2
    l_count = mergeSortCount(l, left, mid, copy)
    r_count = mergeSortCount(l, mid+1, right, copy)
    i, merge_i, j = left, left, mid+1
    merge_count = 0
    while(i <= mid and j <= right):
        if l[i] < l[j]:
            copy[merge_i] = l[i]
            i += 1
        else:
            copy[merge_i] = l[j]
            j += 1
            merge_count += mid - i + 1
        merge_i += 1
    if i == mid + 1:
        copy[merge_i: right+1] = l[j: right+1]
    elif j == right + 1:
        copy[merge_i: right+1] = l[i: mid+1]
    l[left: right+1] = copy[left: right+1]
    return l_count + r_count + merge_count

def main():
    l = [int(num.strip()) for num in open('test.txt').readlines()]
    copy = [0]*(len(l)-1)
    print(mergeSortCount(l, 0, len(l)-1, copy))

main()
