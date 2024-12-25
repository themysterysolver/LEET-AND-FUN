# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count=1
        temp=list1
        while count!=a:
            temp=temp.next
            count+=1
        list1_end=temp
        print('finidnf l1\`s end',temp.val)
        while count!=b+2:
            temp=temp.next
            count+=1
        print('finding l2\'s start',temp.val)
        list2_end=temp
        list1_end.next=list2
        temp=list2
        while temp.next:
            temp=temp.next
        print('the end of list2\'s ending',temp.val)
        temp.next=list2_end
        return list1