# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def display(msg,head):
            print(msg)
            while head:
                print(head.val,end='->')
                head=head.next
            print('\n--------------')
        def findMid(head):
            slow=head
            fast=head
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        def merge(left,right):
            dummy=ListNode()
            temp=dummy
            while left and right:
                if left.val<right.val:
                    temp.next=left
                    left=left.next
                else:
                    temp.next=right
                    right=right.next
                temp=temp.next
            temp.next=left if left else right
            #print('THERE!')
            return dummy.next
        def mergeSort(head):
            if head is None or head.next is None:
                return head
            prev=findMid(head)
            mid=prev.next
            prev.next=None
            #display('MS1:',head)
            #display('MS2:',mid)
            left,right=mergeSort(head),mergeSort(mid)
            #print('HERE!')
            return merge(left,right)
        return mergeSort(head)