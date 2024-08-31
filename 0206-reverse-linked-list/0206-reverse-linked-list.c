/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *temp;
    temp=head;
    while(temp!=NULL){
        printf("%d",temp->val);
        temp=temp->next;
    }
    struct ListNode *prev;
    struct ListNode *nxt;
    struct ListNode *current=head;
    while(current!=NULL){
        if(current==head){
            nxt=current->next;
            prev=current;
            current->next=NULL;
            current=nxt;
        }
        if(current!=NULL){
            nxt=current->next;
            current->next=prev;
            prev=current;
            current=nxt;
        }
    }
    head=prev;
    
    return head;
}