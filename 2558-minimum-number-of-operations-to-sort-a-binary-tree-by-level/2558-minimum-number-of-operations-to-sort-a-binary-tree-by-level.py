# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def find_swaps(nums):
            swaps=0
            target=sorted(nums)
            position={k:idx for idx,k in enumerate(nums)}
            print(sorted,target)
            for i in range(len(nums)):
                if nums[i]!=target[i]:
                    swaps+=1
                    cpos=position[target[i]]
                    nums[i],nums[cpos]=nums[cpos],nums[i]
                    position[nums[cpos]]=cpos
                    position[target[i]]=i
            return swaps
        q=deque([])
        q.append(root)
        t_swaps=0
        while q:
            #print(list(q))
            l=len(q)
            arr=[]
            for i in range(l):
                r=q.popleft()
                arr.append(r.val)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            t_swaps+=find_swaps(arr)
            print(arr,t_swaps)
        return t_swaps