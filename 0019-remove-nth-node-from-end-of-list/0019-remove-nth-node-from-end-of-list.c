/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
   struct ListNode* slow=head;
   struct ListNode* fast=head;
   struct ListNode* prev=NULL;
   int count=1;
   if (n == 1) {
        if (head->next == NULL) {
            free(head);
            return NULL;
        }
    }
    while(count<n){
            fast=fast->next;
            count++;
    }
    if(fast->next==NULL){
        struct ListNode* temp=head;
        head=head->next;
        free(temp);
        return head;
    }
    //printf("%d\n",fast->val);
    while(fast->next!=NULL){
        prev=slow;
        slow=slow->next;
        fast=fast->next;
    }
    //printf("%d\n",prev->val);
    if(prev!=NULL){
        prev->next=slow->next;
    }
    free(slow);
    return head;

}