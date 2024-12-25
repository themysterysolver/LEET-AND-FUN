# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def display(root):
            while root:
                print(root.val,'->',end='')
                root=root.next
            print('\n-----------')
        start=ListNode(0)
        trav=start
        sumi=0
        temp=head
        while temp:
            if temp.val==0 and sumi==0:
                pass
            elif temp.val==0 and sumi!=0:
                trav.next=ListNode(sumi)
                trav=trav.next
                sumi=0
            else:
                sumi+=temp.val
            temp=temp.next
        display(start)
        return start.next

