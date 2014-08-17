class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def sortList(head):
    if not head or not head.next:
        return head
    a,b = splitList(head)
    headA = sortList(a)
    headB = sortList(b)
    mergedHead = mergeList(headA, headB)
    return mergedHead

def splitList(node):
    if not node or not node.next:
        return node, None
    slow = node
    fast = node.next
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next

    secondHead = slow.next
    slow.next = None
    return node, secondHead

def mergeList(a, b):
    if not a:
        return b
    if not b:
        return a
    if a.val < b.val:
        res = a
        a = a.next
    else:
        res = b
        b = b.next
    p = res
    while a and b:
        if a.val < b.val:
            p.next = a
            a = a.next
        else:
            p.next = b
            b = b.next
        p = p.next
    if not a:
        p.next = b
    if not b:
        p.next = a
    return res

def insertionSortList(head):
    if not head or not head.next:
        return head
    prev = head
    node = head.next
    while node:
        if node.val < head.val:
            prev.next = node.next
            node.next = head
            head = node
            node = prev.next
        elif node.val >= prev.val:
            prev = prev.next
            node = node.next
        else:
            p, q = head, head.next
            while q != node:
                if p.val <= node.val and q.val > node.val:
                    print("p", p.val)
                    print("q", q.val)
                    print("prev", prev.val)
                    print("node", node.val)
                    prev.next = node.next
                    p.next = node
                    node.next = q
                    node = prev.next
                    print("p", p.val)
                    print("q", q.val)
                    print("prev", prev.val)
                    print("node", node.val)
                    print("the list is now")
                    printList(head)
                    break
                p= p.next
                q = q.next
    return head

def makeList(a):
    head = ListNode(a[0])
    p = head
    for item in a[1:]:
        node = ListNode(item)
        p.next = node
        p = p.next
    return head

def printList(head):
    while head:
        print(head.val, end =", ")
        head = head.next
    print()

def test():
    a = [3,2,4]
    head = makeList(a)


    #sortedA = sortList(head)
    print("original list")
    printList(head)
    print("sorting")
    sortedList = insertionSortList(head)
    print("after")
    printList(sortedList)

test()
