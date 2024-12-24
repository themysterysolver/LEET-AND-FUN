# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hash=dict()
        l=set()
        for x,y,z in descriptions:
            l.add(x)
            l.add(y)
        for i in l:
            hash[i]=TreeNode(i)
        for k,v in hash.items():
            print(k,v.val)
        for x,y,z in descriptions:
            if z==1:
                hash[x].left=hash[y]
            else:
                hash[x].right=hash[y]
        hasParent={i:[] for i in l}
        for x,y,z in descriptions:
            hasParent[y].append(x)
        print(hasParent)
        for x,y in hasParent.items():
            if len(y)==0:
                return hash[x]