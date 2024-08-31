/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    struct ListNode* temp=head;
    struct ListNode* head2=NULL;
    struct ListNode* prev=NULL;
    struct ListNode* nxt=NULL;
    int count=0;
    if(head==NULL || head->next==NULL){
        return true;
    }
    
    while(temp!=NULL){
        temp=temp->next;
        count++;
    }
    printf("%d\n",count);
    int check=count;
    int count1=count/2;
    int flag=0;
    printf("%d\n",count);
    temp=head;
    while(temp!=NULL){
        if(count1>0){
            printf("%d ",temp->val);
            temp=temp->next;  
            count1--;  
        }
        else{
            if(check%2!=0 && flag==0){
                temp=temp->next;
                flag=1;
            }
            nxt=temp->next;
            temp->next=prev;
            prev=temp;
            temp=nxt;
            //printf("%d",temp->val);
            //temp=temp->next;
        }
        head2=prev;
    }
    temp=head2;
    while(temp!=NULL){
        printf("%d ",temp->val);
        temp=temp->next;
    }
    struct ListNode* temp1=head;
    temp=head2;
    while(temp!=NULL){
        if(temp->val!=temp1->val)
            return false;
        temp=temp->next;
        temp1=temp1->next;
    }
    return true;
}