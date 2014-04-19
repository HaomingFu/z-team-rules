/*
 * A sample answer
 * http://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/
 * Date: April 19, 2014
 */
#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x):val(x), next(NULL){}
};
class Solution {
    public:
        ListNode *removeNthFromEnd(ListNode *head, int n){
            if(head == NULL)
                return NULL;
            
            ListNode dummyHead(0);
            dummyHead.next = head;

            ListNode *fast = &dummyHead;
            ListNode *slow = &dummyHead;

            while(n--)
                fast = fast->next;
            while(!fast && fast->next){
                slow = slow->next;
                fast = fast->next;
            }

            slow->next = slow->next->next;

            return dummyHead.head;
        }
};
