# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []
        hash = defaultdict(int)
        def encode(root):
            if not root:
                return ''
            encoded = str(root.val) + '#' + encode(root.left) + '#' + encode(root.right)
            hash[encoded] += 1
            if hash[encoded] == 2:
                result.append(root)
            return encoded
        print(encode(root))
        return result