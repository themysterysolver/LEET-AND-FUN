# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp:
            temp1=temp
            #print('outter:',temp1.val)
            while temp.next and temp.next.val==temp1.val:
                temp=temp.next
                #print('inner',temp.val)
            temp1.next=temp.next
            temp=temp.next
        return head