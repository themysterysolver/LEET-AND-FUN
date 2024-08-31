# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp=head
        d=dict()
        while temp:
            if temp in d:
                return True
            d[temp]=1
            temp=temp.next
        return False
        