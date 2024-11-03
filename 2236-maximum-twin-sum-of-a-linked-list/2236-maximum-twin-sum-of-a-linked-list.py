# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        temp=slow
        #print(temp)
        prev,nexti=None,None
        while temp:
            nexti=temp.next
            temp.next=prev
            prev=temp
            temp=nexti
        currRev=prev
        maxval=0
        while currRev:
            maxval=max(maxval,currRev.val+head.val)
            currRev=currRev.next
            head=head.next
        return maxval
