# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result=[]
        def dfs(root,path,target):
            if not root:
                return
            path.append(root.val)
            target-=root.val
            if target==0 and not root.left and not root.right:
                result.append(path[:])
            dfs(root.left,path,target)
            dfs(root.right,path,target)
            path.pop()
        dfs(root,[],targetSum)
        return result