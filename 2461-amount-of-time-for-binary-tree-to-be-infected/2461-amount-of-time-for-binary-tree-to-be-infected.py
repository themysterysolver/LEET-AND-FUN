# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        hash=dict()
        q=deque([root])
        #connverted into graph
        while q:
            l=len(q)
            for i in range(l):
                r=q.popleft()
                if r.val not in hash:
                    hash[r.val]=[]
                if r.left:
                    q.append(r.left)
                    hash[r.left.val]=[r.val]
                    hash[r.val].append(r.left.val)
                if r.right:
                    q.append(r.right)
                    hash[r.right.val]=[r.val]
                    hash[r.val].append(r.right.val)
        #print(hash)
        q=deque([start])
        visited=set()
        visited.add(start)
        count=0
        while q:
            l=len(q)
            for i in range(l):
                n=q.popleft()
                for node in hash[n]:
                    if node not in visited:
                        visited.add(node)
                        q.append(node)
            count+=1
        return count-1
