# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def display(nums):
            for r in nums:
                print(r.val,end=' ')
            print('\n----------')

        paths=[]
        def dfs(root,key,path):
            if not root:
                return 
            path.append(root)
            if root.val==key.val:
                paths.append(path[:])
            else:
                dfs(root.left,key,path)
                dfs(root.right,key,path)
            path.pop()
        dfs(root,p,[])
        dfs(root,q,[])
        print(len(paths))
        display(paths[0])
        display(paths[1])
        ans=root
        if len(paths[1])<len(paths[0]):
            l=len(paths[1])
        else:
            l=len(paths[0])
        for i in range(l):
            #print(i,paths[0][i].val,paths[1][i].val,paths[0][i].val==paths[1][i].val,paths[0][i]==paths[1][i])
            if paths[0][i]==paths[1][i]:
                ans=paths[0][i]
                #print('ans',i,ans.val)
                #print('--')
            else:
                break
        return ans