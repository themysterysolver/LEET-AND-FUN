# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        count = 0
        while q:
            l = len(q)
            flag = False
            for _ in range(l):
                node = q.popleft()
                if flag and node:
                    return False
                if not node:
                    flag = True
                    continue
                q.append(node.left)
                q.append(node.right) 
            #print([el.val for el in q])
            count+=1
            if flag and q and q[0]:
                return False
        return True