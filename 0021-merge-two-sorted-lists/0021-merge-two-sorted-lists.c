/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if(list1==NULL && list2==NULL)
        return NULL;
    else if(list1==NULL)
        return list2;
    else if(list2==NULL)
        return list1;
    
    struct ListNode* list3;
    list3=(struct ListNode*)malloc(sizeof(struct ListNode));
    if(list1->val<=list2->val){
            list3->val=list1->val;
            list1=list1->next;
        }
    else if(list1->val>list2->val){
            list3->val=list2->val;
            list2=list2->next;
        }
    struct ListNode* temp=list3;
    while(list1!=NULL && list2!=NULL){
        temp->next=(struct ListNode*)malloc(sizeof(struct ListNode));
        temp=temp->next;
        if(list1->val<=list2->val){
            temp->val=list1->val;
            list1=list1->next;
        }
        else if(list1->val>list2->val){
            temp->val=list2->val;
            list2=list2->next;
        }
    }
    if(list1==NULL && list2!=NULL)
        while(list2!=NULL){
            temp->next=(struct ListNode*)malloc(sizeof(struct ListNode));
            temp=temp->next;
            temp->val=list2->val;
            list2=list2->next;
        }

    else if(list2==NULL && list1!=NULL)
        while(list1!=NULL){
            temp->next=(struct ListNode*)malloc(sizeof(struct ListNode));
            temp=temp->next;
            temp->val=list1->val;
            list1=list1->next;
        }
    temp->next=NULL;
    return list3;
    
}