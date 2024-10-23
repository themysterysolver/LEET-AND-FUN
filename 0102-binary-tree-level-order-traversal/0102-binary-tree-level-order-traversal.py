# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=[]
        result=[]
        q.append(root)
        while len(q)>0:
            levelList=[]
            l=len(q)
            for i in range(l):
                r=q.pop(0)
                levelList.append(r.val)
                if r.left is not None:
                    q.append(r.left)
                if r.right is not None:
                    q.append(r.right)
            result.append(levelList)
        return result

        