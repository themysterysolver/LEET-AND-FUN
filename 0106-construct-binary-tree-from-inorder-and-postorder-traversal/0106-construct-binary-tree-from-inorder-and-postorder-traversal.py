# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        map={val:idx for idx,val in enumerate(inorder)}
        postorderIdx=[len(postorder)-1]
        def helper(left,right):
            if left>right:
                return None
            value=postorder[postorderIdx[0]]
            postorderIdx[0]-=1
            newNode=TreeNode(value)
            idx=map[value]
            newNode.right=helper(idx+1,right)
            newNode.left=helper(left,idx-1) 
            return newNode
        return helper(0,len(inorder)-1)