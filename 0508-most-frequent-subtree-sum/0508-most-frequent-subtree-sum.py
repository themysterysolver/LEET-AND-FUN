# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        hash = defaultdict(int)
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            sumx = left+right+root.val
            hash[sumx] += 1
            return sumx
        dfs(root)
        #print(hash)
        maxi = max(hash.values())
        count = 0
        ans = []
        for key,val in hash.items():
            if val == maxi:
                ans.append(key)
        return ans