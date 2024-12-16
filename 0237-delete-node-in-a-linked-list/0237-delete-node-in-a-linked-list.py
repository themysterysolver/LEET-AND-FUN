# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp=node
        while temp!=None:
            #print(node)
            if temp.next==None:
                prev.next=None
                break
            prev=temp
            temp=temp.next
            prev.val=temp.val

        