class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adL = defaultdict(list)
        indegree = defaultdict(int)
        for u,v in adjacentPairs:
            adL[u].append(v)
            adL[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
        
        def BFS(start):
            ans = []
            q = deque([start])
            visited =set()
            visited.add(start)
            while q:
                node = q.pop()
                ans.append(node)
                for nei in adL[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            return ans
        for key,val in indegree.items():
            if val == 1:
                ans = BFS(key)
                break
        return ans