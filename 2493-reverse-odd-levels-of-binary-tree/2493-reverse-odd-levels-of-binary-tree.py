# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(q):
            start,end=0,len(q)-1
            while start<end:
                q[start].val,q[end].val=q[end].val,q[start].val
                start+=1
                end-=1
            return q
        def printd(lvl,q):
            print(lvl,':',end=' ')
            for i in q:
                print(i.val,end=' ')
            print('\n------------------------')
        q=deque([root])
        lvl=0
        while q:
            l=len(q)
            printd(lvl,q)
            if lvl%2==1:
                q=reverse(q)
            for i in range(l):
                r=q.popleft()
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            lvl+=1
        return root