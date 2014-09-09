# From: https://oj.leetcode.com/problems/reorder-list/
# Accepted
# Date: May 22, 2014
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        fast = head
        slow = head
        while fast.next :
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
            slow = slow.next
        p=self.reverse(slow.next)
        slow.next = None
        pf= head
        while  p:
            temps = p
            p = p.next
            tempf = pf.next
            pf.next = temps
            temps.next =  tempf
            pf = tempf

    def reverse(self, head):
        p = head.next
        head.next = None
        while p:
            ptmp = p
            p = p.next
            ptmp.next = head
            head = ptmp
        return head

if __name__ == "__main__":
    head = ListNode(1)
    p = head
    for i in range(2, 6):
        p.next = ListNode(i)
        p = p.next
    s = Solution()
    head = s.reverse(head)
    while head:
        print(head.val)
        head = head.next


