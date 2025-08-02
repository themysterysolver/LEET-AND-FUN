# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp:
            slow = temp
            fast = temp.next
            while fast and fast.val == slow.val:
                fast = fast.next
            slow.next = fast
            temp = fast
        return head