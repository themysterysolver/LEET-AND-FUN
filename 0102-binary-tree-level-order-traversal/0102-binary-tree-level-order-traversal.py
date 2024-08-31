# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        q=[]
        rlist=[]
        q.append(root)
        while len(q)>0:
            ans=[]
            l=len(q)
            for i in range(l):
                node=q.pop(0)
                ans.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            rlist.append(ans)
        return rlist

        