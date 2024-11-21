# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash=dict()
        temp=headA
        while temp!=None:
            hash[temp]=temp.val
            temp=temp.next
        temp=headB
        while temp!=None:
            if temp in hash:
                return temp
            temp=temp.next
        return None