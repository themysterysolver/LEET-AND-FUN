# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=head
        prev=None
        nexti=None
        if temp is None:
            return head
        while temp is not None:
            nexti=temp.next
            temp.next=prev
            prev=temp
            temp=nexti
        return prev

        
       

        
        