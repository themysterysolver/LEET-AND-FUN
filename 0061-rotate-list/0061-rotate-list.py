# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k==0:
            return head
        if head.next is None:
            return head
        temp=head
        count=0
        prev=None
        while temp is not None:
            prev=temp
            temp=temp.next
            count+=1
        print (count)
        temp=head
        k=k%count
        if k==0:
            return head
        for _ in range(count-k-1):
            temp=temp.next
        head2=temp.next
        temp.next=None
        prev.next=head
        print(temp.val)
        return head2