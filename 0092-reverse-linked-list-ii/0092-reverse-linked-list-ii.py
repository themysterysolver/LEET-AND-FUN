# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        curr = 0
        def dis(ll):
            while ll:
                print(ll.val,end='->')
                ll=ll.next
            #print('----------')
        temp = head
        dummy = ListNode(0,head)
        prev = dummy
        for _ in range(left-1):
            prev = temp
            temp = temp.next
        leftStart = prev

        #dis(temp)
        #dis(prev)

        prev = None
        end = temp
        for _ in range(right-left+1):
            nexti = temp.next
            temp.next = prev
            prev = temp
            temp = nexti
        
        leftStart.next = prev
        end.next = temp
        return dummy.next
        
