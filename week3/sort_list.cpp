/* Accepted.
 * By Yao
 * March 27, 2014
 * From http://oj.leetcode.com/problems/sort-list/
 */

#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode * next;
    ListNode(int x): val(x), next(NULL){};
};

class Solution {
    public:
        ListNode *sortList(ListNode *head){
            if(head ==NULL || head->next == NULL)
                return head;

            int len =0;
            ListNode *it = head;
            while(it){
                len++;
                it= it->next;
            }
            //divide the list into two halves
            ListNode * lList, *rList ;
            lList = head;
            for(int i=1;i<len/2;++i)
                head = head->next;
            rList = head->next;
            head->next = NULL;

            lList = sortList(lList);
            rList = sortList(rList);

            //to merge the two sorted lists
            if(lList->val < rList->val){
                head = lList;
                lList = lList->next;
            }
            else{
                head = rList;
                rList = rList->next;
            }
            ListNode *end=head;

            while(lList && rList){
                if(lList->val < rList->val){
                    end->next = lList;
                    lList = lList->next;
                    end = end->next;
                }
                else{
                    end->next = rList;
                    rList = rList->next;
                    end = end->next;
                }
            }
            if(lList==NULL)
                end->next = rList;
            else
                end->next = lList;

            return head;
        }
};

int main(){
    Solution mysolution;
    ListNode *head, *end;

    head=new struct ListNode(10);
    end = head;
    for(int i=9;i>0;--i){
       end->next = new struct ListNode(i);
       end = end->next;
    }
    end=NULL;

    head = mysolution.sortList(head);
    while(head){
        cout<<head->val<<" ";
        head = head->next;
    }
    cout<<endl;
}
