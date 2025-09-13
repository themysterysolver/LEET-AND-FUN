# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        sameGroup = False
        count = 0
        s = set(nums)
        temp = head
        while temp:
            if sameGroup:
                if temp.val in s:
                    temp = temp.next
                    continue
                else:
                    sameGroup = False
            else:
                if temp.val in s:
                    count+=1
                    sameGroup = True
            temp = temp.next
        return count