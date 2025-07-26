class TreeNode:
    def __init__(self,v=None,l=None,r=None):
        self.left = l
        self.right = r
        self.val = v
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def inorder(root):
            if root:
                print(root.val)
                inorder(root.left)
                inorder(root.right)

        hash = {i:TreeNode(i) for i in range(len(parents))}
        for idx,parent in enumerate(parents):
            if parent == -1:
                continue
            if hash[parent].left:
                hash[parent].right = hash[idx]
            else:
                hash[parent].left = hash[idx]
        #inorder(hash[0])
        totalCount = len(parents) #total no of ndoes
        reduced = totalCount - 1 #helps in calculating the remainign component length
        #maxi = float('-inf')
        result = []
        def findMaxScore(root):
            #nonlocal maxi
            if not root:
                return 0
            left = findMaxScore(root.left)
            right = findMaxScore(root.right)
            remaining = reduced - (left+right)
            score = 1
            for s in [left,right,remaining]:
                if s>0:
                    score *= s
            result.append(score)
            return left+right+1
        findMaxScore(hash[0])
        return result.count(max(result))
