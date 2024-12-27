# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        def display(root):
            while root:
                print(root.val,'->',end='')
                root=root.next
            print('\n--------------')
        prev,temp=ListNode(0),head
        print('p c n')
        start=prev
        start.next=head
        while temp:
            if temp.next and temp.val==temp.next.val:
                while temp.next and temp.val==temp.next.val:
                    temp=temp.next
                #print(prev.val,temp.val,temp.next.val)
                temp=temp.next
                prev.next=temp
                #print(prev.val,temp.val,temp.next.val)
                print('-----------------------')
            else:
                prev=temp
                temp=temp.next
        print('prev val at end!:',prev.val)
        display(head)
        display(start)
        if head.next and head.val!=head.next.val:
            return head
        else:
            return start.next
        
