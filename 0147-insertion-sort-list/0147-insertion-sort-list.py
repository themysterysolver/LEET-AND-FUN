# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(-5000,head)
        lastSorted=head
        temp=head.next
        while temp:
            if temp.val>=lastSorted.val:
                lastSorted=temp
            else:
                prev=dummy
                while prev.next.val<=temp.val:
                    prev=prev.next
                lastSorted.next=temp.next
                temp.next=prev.next
                prev.next=temp
            temp=lastSorted.next
        return dummy.next