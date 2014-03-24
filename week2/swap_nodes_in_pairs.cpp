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
            head = head->next;
        }
        return fixed;
    }
};

int main(){
    ListNode* mylist = new ListNode(1);
    mylist->next = new ListNode(2);

    Solution mysolution;
    mylist=mysolution.swapPairs(mylist);
    cout<<mylist->val<<endl<<mylist->next->val<<endl;

    return 0;
}
