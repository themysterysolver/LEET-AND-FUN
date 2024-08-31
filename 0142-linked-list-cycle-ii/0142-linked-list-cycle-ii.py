# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pos=-1
        temp=head
        d=dict()
        while temp:
            if temp in d:
                return temp
            pos=pos+1
            d[temp]=pos
            temp=temp.next
        return None
        