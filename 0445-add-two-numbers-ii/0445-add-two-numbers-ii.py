# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,root):
        prev,nexti=None,None
        temp=root
        while temp:
            nexti=temp.next
            temp.next=prev
            prev=temp
            temp=nexti
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1=self.rev(l1)
        l2=self.rev(l2)
        print(l1)
        print(l2)
        carry=0
        root=n=ListNode(0)
        while l1 or l2 or carry:
            v1=v2=0
            if l1:
                v1=l1.val
                l1=l1.next
            if l2:
                v2=l2.val
                l2=l2.next
            carry,value=divmod(v1+v2+carry,10)
            n.next=ListNode(value)
            n=n.next
        return self.rev(root.next)
