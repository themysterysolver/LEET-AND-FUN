# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root):
        # Initialize pointers to track swapped nodes and previous node in inorder
        self.first = None
        self.second = None
        self.prev = None

        def inorder(node):
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Detect violation: previous node's value should be less than current node's value
            if self.prev and self.prev.val > node.val:
                # First time violation encountered
                if not self.first:
                    self.first = self.prev
                # Always update second node to current node when violation detected
                self.second = node
            
            # Update previous node
            self.prev = node
            
            # Traverse right subtree
            inorder(node.right)
        
        # Perform inorder traversal to find nodes to swap
        inorder(root)
        
        # Swap the values of the two nodes to fix the BST
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
