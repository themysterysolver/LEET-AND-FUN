"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        def dfs(root):
            temp = root
            prev = temp
            while temp:
                #print(temp.val)
                if temp.child:
                    nextNode = temp.next
                    temp.next = temp.child
                    temp.child.prev = temp
                    temp.child = None

                    lastNode = dfs(temp.next)
                    if lastNode:
                        lastNode.next = nextNode
                        if nextNode:
                            nextNode.prev = lastNode
                    temp = lastNode
                prev = temp
                temp = temp.next
            return prev
        dfs(head) 

        return head