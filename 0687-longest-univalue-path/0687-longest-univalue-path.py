# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxi = [0]
        def dfs(root):
            if not root:
                return (-2000,0)
            lval,lcount = dfs(root.left)
            rval,rcount = dfs(root.right)
            maxi[0] = max(maxi[0],lcount,rcount)
            print(root.val,lval,lcount,rval,rcount,maxi[0])
            if lval == -2000 and rval == -2000:
                return (root.val,0)
            elif lval == root.val and rval == root.val:
                maxi[0] = max(maxi[0],lcount+rcount+2)
                return (root.val,max(lcount,rcount)+1)
            elif lval == root.val:
                return (root.val,lcount+1)
            elif rval == root.val:
                return (root.val,rcount+1)
            else:
                return (root.val,0)
        val,c = dfs(root)
        maxi[0] = max(maxi[0],c)
        return maxi[0] 