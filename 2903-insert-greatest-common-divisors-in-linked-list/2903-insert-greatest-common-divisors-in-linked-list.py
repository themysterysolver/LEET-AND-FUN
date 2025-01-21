# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def GCD(a,b):
            while b:
                a,b=b,a%b
            return a
        def display(head):
            while head:
                print(head.val,end='->')
                head=head.next
            print('--------------')
        temp=head
        if not head.next or not head:
            return head
        while temp:
            #display(head)
            if temp.next:
                nxt=temp.next
                cval=temp.val
                nval=nxt.val
                nnode=ListNode(GCD(cval,nval))
                temp.next=nnode
                nnode.next=nxt
                temp=nxt
            else:
                temp=temp.next
        #display(head)
        return head