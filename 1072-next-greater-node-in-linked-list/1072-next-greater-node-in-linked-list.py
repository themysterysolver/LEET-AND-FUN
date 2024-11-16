# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack=[]
        temp=head
        result=[]
        i=0
        while temp!=None:
            result.append(0)
            while stack and stack[-1][0]<temp.val:
                val,idx=stack.pop()
                result[idx]=temp.val
            stack.append((temp.val,i))
            i+=1
            temp=temp.next
        return result