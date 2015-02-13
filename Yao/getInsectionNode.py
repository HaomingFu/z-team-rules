#!/usr/bin/env python
# encoding: utf-8

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

def getIntersection(headA, headB):
    if not headB or not headB:
        return None

    lenA = lenB = 1
    iterA = headA; iterB = headB
    while iterA.next:
        lenA += 1
        iterA = iterA.next
    while iterB.next:
        lenB += 1
        iterB = iterB.next

    if iterA != iterB:
        return None

    if lenA > lenB:
        longer = headA
        short = headB
        diff = lenA - lenB
    else:
        longer = headB
        short = headA
        diff = lenB - lenA

    while diff:
        longer = longer.next
        diff -= 1

    while longer:
        if longer == short:
            return longer
        longer = longer.next
        short = short.next
    return None

if __name__ == "__main__":
    headA = Node(1)
    headB = Node(2)
    headA.next = headB
    res = getIntersection(headA, headB)
    if res:
        print("Exits, value: ", res.value)
    else:
        print("None")

