# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Do not return anything, modify head in-place instead.
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def display(msg,temp):
            print(msg)
            while temp:
                print(temp.val,end='->')
                temp=temp.next
            print()
        def breakIt(temp):
            slow,fast=temp,temp
            fast=slow.next.next
            while fast:
                if fast.next is None:
                    slow=slow.next
                    break
                slow=slow.next
                fast=fast.next.next
            new=slow.next
            slow.next=None
            return temp,new
        def rev(temp):
            prev,nexti=None,None
            while temp:
                nexti=temp.next
                temp.next=prev
                prev=temp
                temp=nexti
            return prev
            
        if head.next is None or head.next.next is None:
            return head
        
        temp1,temp2=breakIt(head)
        #display('break-1',temp1)
        #display('break-2',temp2)
        temp2=rev(temp2)
        #display('rev break-2',temp2)
        temp=temp1
        while temp1 and  temp1.next:
            #display(temp)
            temp3=temp2.next
            temp2.next=temp1.next
            temp1.next=temp2
            temp2=temp3
            temp1=temp1.next.next
        if temp2:
            temp1.next=temp2
        return temp


            
        
        