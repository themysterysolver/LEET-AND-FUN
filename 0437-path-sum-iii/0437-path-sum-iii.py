# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def dfs(r,ts):
            if not r:
                return
            if ts==r.val:
                self.ans+=1
            dfs(r.left,ts-r.val)
            dfs(r.right,ts-r.val)
            return
        s=set()
        q=deque([root])
        while q:
            n=q.popleft()
            s.add(n)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        print(len(s))
        for r in s:
            dfs(r,targetSum)
        print(self.ans)
        return self.ans
                



        