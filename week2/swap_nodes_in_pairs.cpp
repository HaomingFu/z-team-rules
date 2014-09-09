/**
 *   Definition for singly-linked list.
 *   struct ListNode {
 *       int val;
 *       ListNode *next;
 *       ListNode(int x) : val(x), next(NULL) {}
 *   };
 */

#include <iostream>

using namespace std;

typedef struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL){}
}ListNode;

class Solution {
public:
    ListNode *swapPairs(ListNode *head) {
        if(head==NULL)
            return NULL;
        ListNode *temp = head;
        ListNode *fixed = head;
        int value;
        while(head->next){
            head=head->next;
            value = temp->val;
            temp->val = head->val;
            head->val = value;
            temp = head->next;
            if(head->next)
                head = head->next;
        }
        return fixed;
    }
};

int main(){
    ListNode* mylist = new ListNode(1);
    mylist->next = new ListNode(2);
    mylist->next->next = new ListNode(3);
    mylist->next->next->next = new ListNode(4);

    Solution mysolution;
    mylist=mysolution.swapPairs(mylist);
    cout<<mylist->val<<endl<<mylist->next->val<<endl;
    cout<<mylist->next->next->val<<endl;
    cout<<mylist->next->next->next->val<<endl;

    return 0;
}
