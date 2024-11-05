class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l=len(isConnected)
        visited=[False]*l
        count=0
        def BFS(city):
            q=deque([city])
            visited[city]=True
            while q:
                current=q.popleft()
                for neighbour in range(l):
                    if not visited[neighbour] and isConnected[current][neighbour]==1:
                        q.append(neighbour)
                        visited[neighbour]=True
        for i in range(l):
            if not visited[i]:
                BFS(i)
                count+=1
        return count