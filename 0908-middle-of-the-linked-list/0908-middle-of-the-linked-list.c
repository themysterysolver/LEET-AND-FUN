/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode *rabbit=head;
    struct ListNode *tortoise=head;
    while(rabbit!=NULL){
        rabbit=rabbit->next;
        if(rabbit==NULL){
            return tortoise;
        }
        tortoise=tortoise->next;
        rabbit=rabbit->next;
        
    }
    return tortoise;
    
}