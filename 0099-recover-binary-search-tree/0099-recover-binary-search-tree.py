# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorderArr=[]
        hash=dict()
        def inorder(root):
            if root:
                inorder(root.left)
                inorderArr.append(root.val)
                hash[root.val]=root
                inorder(root.right)
        inorder(root)
        #print(inorderArr)
        sortedArr=sorted(inorderArr)
        #print(sortedArr)
        for i in range(len(inorderArr)):
            if inorderArr[i]!=sortedArr[i]:
                hash[inorderArr[i]].val,hash[sortedArr[i]].val=sortedArr[i],inorderArr[i]
                break
