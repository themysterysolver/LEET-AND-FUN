"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        def display(temp):
            while temp:
                print(temp.val,'->',end='')
                temp=temp.next
            print('\n-----------------------')
        #display(head)
        hash=dict()
        temp=head
        while temp:
            hash[temp]=Node(temp.val)
            temp=temp.next
        #print('hash')
        '''for k,v in hash.items():
            display(v)'''
        temp=head
        i=0
        #print('fabricating')
        while temp:
            if temp.next:
                hash[temp].next=hash[temp.next]
            #print(i)
            temp=temp.next
            #i+=1        
        '''for k,v in hash.items():
            display(v)'''
        temp=head
        #print('fabricating random')
        while temp:
            if temp.random:
                hash[temp].random=hash[temp.random]
            temp=temp.next
        return hash[head]
