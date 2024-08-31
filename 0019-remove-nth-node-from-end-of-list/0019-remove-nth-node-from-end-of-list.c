/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
   struct ListNode* current=head;
   int count=0;
   while(current!=NULL){
    count++;
    current=current->next;
   }
   printf("%d\n",count);
   int del=count-n+1;
   printf("%d\n",del);
   current=head;
   del--;
   struct ListNode* prev=NULL;
   if(del==0){
        struct ListNode* temp=head;
        head=head->next;
        free(temp);
        return head;
   }
    while(del!=0){
         prev=current;
         current=current->next;
         del--;
    }
    printf("C.VALUE:%d\n",current->val);
    printf("PREV.VALUE:%d",prev->val);
    prev->next=current->next;
    free(current);
    return head;
}