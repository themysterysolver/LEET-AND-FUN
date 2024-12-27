# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def DFS(root,csum):
            if not root:
                return
            if not root.left and not root.right:
                result.append(csum+str(root.val))
            if root.left:
                DFS(root.left,csum+str(root.val))
            if root.right:
                DFS(root.right,csum+str(root.val))
        result=[]
        DFS(root,"")
        print(result)
        result=[int(binary,2) for binary in result]
        return sum(result)