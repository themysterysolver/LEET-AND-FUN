# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 1
        def BFS(root):
            q=deque([root])
            maximum=[]
            maximum.append(root.val)
            while q:
                l=len(q)
                value=0
                for i in range(l):
                    tempRoot=q.popleft()
                    if tempRoot.left:
                        q.append(tempRoot.left)
                        value+=tempRoot.left.val
                    if tempRoot.right:
                        q.append(tempRoot.right)
                        value+=tempRoot.right.val
                maximum.append(value)
            maximum.pop()
            print(maximum)
            #print(list(q))
            return maximum.index(max(maximum))+1
        return BFS(root)
        