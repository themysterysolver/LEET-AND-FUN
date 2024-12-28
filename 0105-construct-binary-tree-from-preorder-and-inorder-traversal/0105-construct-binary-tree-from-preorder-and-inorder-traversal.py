# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map={val:idx for idx,val in enumerate(inorder)}
        preorderIdx=[0]
        def builder(left,right):
            if left>right:
                return None
            newNode=TreeNode(preorder[preorderIdx[0]])
            idx=map[preorder[preorderIdx[0]]]
            preorderIdx[0]+=1
            newNode.left=builder(left,idx-1)
            newNode.right=builder(idx+1,right)
            return newNode
        return builder(0,len(inorder)-1)#for manupulating inorder array array to find left and right subtreee