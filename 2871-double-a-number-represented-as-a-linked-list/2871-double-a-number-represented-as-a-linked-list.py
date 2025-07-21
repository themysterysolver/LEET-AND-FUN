# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def display(t):
            while t:
                print(t.val,end='->')
                t = t.next
            print('\n-------------------')
        def rev(h):
            prev = None
            while h:
                nexti = h.next
                h.next = prev
                prev = h
                h = nexti
            return prev

        head1 = rev(head)
        #display(head1)
        temp = head1
        carry = 0
        while carry!=0 or temp:
            if temp:
                num = temp.val*2 + carry
                temp.val = num%10
                carry = num//10
                prev = temp
                temp = temp.next
            else:
                prev.next = ListNode(carry)
                carry = 0
        #display(head1)
        return rev(head1)
