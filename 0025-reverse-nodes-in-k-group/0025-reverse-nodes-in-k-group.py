# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        flag = True
        for _ in range(k):
            if temp:
                temp = temp.next
            else:
                flag = False
                break
        if not flag:
            return head
        prev = None
        temp = head
        for _ in range(k):
            nexti = temp.next
            temp.next = prev
            prev = temp
            temp = nexti
        head.next = self.reverseKGroup(temp,k)
        return prev