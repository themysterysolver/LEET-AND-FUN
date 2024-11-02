# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def BFS(root):
            q=deque([])
            if not root:
                return []
            result=[]
            q.append(root)
            level=0
            while q:
                l=len(q)
                ans=[]
                for i in range(l):
                    r=q.popleft()
                    if r.left:
                        q.append(r.left)
                    if r.right:
                        q.append(r.right)
                    if level%2==0:
                        ans.append(r.val)
                    else:
                        ans.insert(0,r.val)
                result.append(ans) 
                level+=1
            return result
        return BFS(root)