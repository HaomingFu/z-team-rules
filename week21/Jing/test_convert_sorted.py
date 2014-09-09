class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def sortedListToBST(head):
    if not head:
        return head
    if not head.next:
        return TreeNode(head.val)
    head, root, nextNode = findRoot(head)
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(nextNode)
    return root
def findRoot(head):
    slow = q = head
    fast = head.next
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            q = slow
            slow = slow.next
    nextNode = slow.next
    root = TreeNode(slow.val)
    q.next = None
    if q == slow:
        head = None
    return head, root, nextNode


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

def printTree(root):
    if not root:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)
def test():
    a = [1,3]
    head = makeList(a)
    printList(head)
    tree = sortedListToBST(head)
    printTree(tree)
    a = [3, 5, 8]
    head = makeList(a)


    #sortedA = sortList(head)
    printList(head)
    tree = sortedListToBST(head)
    printTree(tree)

test()
