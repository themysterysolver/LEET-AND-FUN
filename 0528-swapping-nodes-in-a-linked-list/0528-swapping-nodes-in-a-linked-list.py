# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp is not None:
            count=count+1
            temp=temp.next
        start=1
        print(count)
        temp=head
        first=last=head
        for i in range(k-1):
            first=first.next
        temp=first
        while temp.next:
            last=last.next
            temp=temp.next
        last.val,first.val=first.val,last.val
        return head