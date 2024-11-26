# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            newRoot=TreeNode(val,root,None)
            return newRoot
        if depth==2:
            root.left=TreeNode(val,root.left,None)
            root.right=TreeNode(val,None,root.right)
            return root
        def BFS():
            d=1
            q=deque([root])
            while q:
                l=len(q)
                for i in range(l):
                    r=q.popleft()
                    if r.left:
                        q.append(r.left)
                    if r.right:
                        q.append(r.right)
                d+=1
                if d==depth-1:
                    break
            for i in q:
                 print(i.val)
            print('------------')
            for r in q:
                print(r.val)
                r.left=TreeNode(val,r.left,None)
                r.right=TreeNode(val,None,r.right)
            print(root)
            return root   
        return BFS()