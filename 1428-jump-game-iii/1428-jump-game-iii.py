class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue=deque([start])
        visited=[False]*len(arr)
        visited[start]=True

        print(arr)
        print(list(queue))
        print('-------------------------')
        while queue:
            l=len(queue)
            for i in range(l):
                curr=queue.popleft()
                if arr[curr]==0:
                    return True
                else:
                    if curr+arr[curr]<len(arr) and not visited[curr+arr[curr]]:
                        queue.append(curr+arr[curr])
                        visited[curr+arr[curr]]=True
                    if curr-arr[curr]>=0 and not visited[curr-arr[curr]]:
                        queue.append(curr-arr[curr])
                        visited[curr-arr[curr]]=True
                print(list(queue))
        return False
