# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if not root:
            return []
        q=deque([root])
        def maxi(nums):
            re=[r.val for r in nums]
            return max(re)
                    
        while q:
            l=len(q)
            result.append(maxi(q))
            for i in range(l):
                r=q.popleft()
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            
        return result