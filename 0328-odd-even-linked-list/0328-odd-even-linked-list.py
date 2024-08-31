# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next==None:
            return head
        odd=head
        even=head.next
        evenhead=even
        #odd,even,evenhead=head,head.next,even
        while odd.next!=None and even.next!=None:
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        odd.next=evenhead
        return head  
