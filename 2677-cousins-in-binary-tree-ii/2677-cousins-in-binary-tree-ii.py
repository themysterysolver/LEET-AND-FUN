# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def BFS1(root):
            q=deque([root])
            levelsum=[]
            while q:
                l=len(q)
                suml=0
                for _ in range(l):
                    r=q.popleft()
                    suml+=r.val
                    if r.left:
                        q.append(r.left)
                    if r.right:
                        q.append(r.right)
                levelsum.append(suml)
            return levelsum
        def BFS2(root,levelsum):
            q=deque([root])
            root.val=0
            level=1
            while q:
                l=len(q)
                for _ in range(l):
                    r=q.popleft()
                    sibling_sum=0
                    if r.left:
                        sibling_sum+=r.left.val
                    if r.right:
                        sibling_sum+=r.right.val
                    if r.left:
                        r.left.val=levelsum[level]-sibling_sum
                        q.append(r.left)
                    if r.right:
                        r.right.val=levelsum[level]-sibling_sum
                        q.append(r.right)
                level+=1
            return root            
        levelsum=BFS1(root)
        print(levelsum)
        return BFS2(root,levelsum)