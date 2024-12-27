# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result=[]
        def display(head):
            while head:
                print(head.val,'->',end='')
                head=head.right
            print('\n-----------------------')
                
        def preorder(root):
            if root:
                result.append(root)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        #print('resut',result)
        current=TreeNode(0)
        temp=current
        for i in result:
            i.left=None
            temp.right=i
            temp=temp.right
        #display(current.right)
        return current.right