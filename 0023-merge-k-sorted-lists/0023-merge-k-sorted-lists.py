# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        mid=len(lists)//2
        left=self.mergeKLists(lists[:mid])
        right=self.mergeKLists(lists[mid:])
        return self.merge(left,right)
    def merge(self,l1,l2):
        current=ListNode(0)
        temp=current
        while l1 and l2:
            if l1.val<l2.val:
                temp.next=ListNode(l1.val)
                l1=l1.next
                temp=temp.next
            else:
                temp.next=ListNode(l2.val)
                l2=l2.next
                temp=temp.next
        temp.next=l1 or l2
        return current.next

                



        