/*
 *
 */

#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x): val(x), next(NULL){};
};

class Solution{
    public:
        ListNode* insertionSortList(ListNode* head){
            if(!head || !(head->next))
                    return head;
            
            ListNode * current, *last,  *it;
                   
            last = head;
            it = head;
            current = head->next;
            while(current){
                if(last->val <= current->val)
                {
                    last = current;
                    current = current->next;
                }
                else{
                   last->next = current->next;
                   if(current->val < head->val){
                       current->next = head;
                       head = current;
                       current = last->next;
                   }
                   else{
                       it =head;
                       while(it!=last){
                           if(it->val < current->val && it->next->val >current->val){
                               current->next = it->next;
                               it->next = current;
                               current = last->next;
                               break;
                           }
                           else
                               it = it->next;
                       }
                   }
                }
            }

            return head;
        }
};
int main(){
    ListNode* head, *end;
    int testNum[10]={4, 19, 14, 5, -3, 1, 8, 5, 11, 15};
    head = new ListNode(4);
    if (head == NULL) cout<<"Failed";
    end = head;
    for(int i=1;i<10;++i){
        end->next =  new ListNode(testNum[i]);
        cout << end->val << endl;
        end = end->next;
    }
    Solution mysolution;

    cout<<"Before testing: "<<endl;
    ListNode *h = head;
    cout<<h->val<<endl;
    cout<<h->next->val<<endl;
    while(1){
        cout<<h->val<<" ";
        h = h->next;
        if(h==NULL)
            break;
    }
    head = mysolution.insertionSortList(head);
    while(head){
        cout<<head->val<<" ";
        head = head->next;
    }
    cout<<endl;
}
