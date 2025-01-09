# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        def display(head):
            temp=head
            while temp:
                print(temp.val,'->',end='')
                temp=temp.next
            print('---------')
        s=set(nums)
        dummy=ListNode(0,head)
        #display(dummy)
        temp=dummy
        prev=dummy
        while temp:
            if temp.val in s:
                while temp and temp.val in s:
                    temp=temp.next
                prev.next=temp
            prev=temp
            if temp:
                temp=temp.next
        #display(dummy)
        return dummy.next

        