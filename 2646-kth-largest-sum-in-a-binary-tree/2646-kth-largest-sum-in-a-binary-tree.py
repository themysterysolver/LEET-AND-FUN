# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def BFS(root,k):
            queue=deque([root])
            heap=[]
            while queue:
                l=len(queue)
                sum=0
                for i in range(l):
                    #print('heap',list(heap))
                    #print(list(queue))
                    r=queue.popleft()
                    #print('val',r.val)
                    sum+=r.val
                    if r.left is not None:
                        #print('r.left',r.left.val,'----',r.val)
                        queue.append(r.left)
                    if r.right is not None:
                        #print('r.right',r.right.val,'----',r.val)
                        queue.append(r.right)
                #print(sum)
                heapq.heappush(heap,-sum)
            for i in range(k-1):
                if heap:
                    heapq.heappop(heap)
            if heap:
                return -heapq.heappop(heap)
            else:
                return -1
        return BFS(root,k)
        