# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        shead,bhead=ListNode(),ListNode()
        temp1,temp2=shead,bhead
        while head:
            if head.val<x:
                shead.next=ListNode(head.val)
                shead=shead.next
            else:
                bhead.next=ListNode(head.val)
                bhead=bhead.next
            head=head.next
        shead.next=temp2.next
        bhead.next=None
        return temp1.next