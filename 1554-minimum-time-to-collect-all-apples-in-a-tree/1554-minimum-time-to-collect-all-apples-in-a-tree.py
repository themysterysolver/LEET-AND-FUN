class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adL = defaultdict(list)
        for u,v in edges:
            adL[u].append(v)
            adL[v].append(u)
        
        def dfs(root,parent):
            total = 0
            for child in adL[root]:
                if child == parent:
                    continue
                c = dfs(child,root)
                if c>0 or hasApple[child]:
                    total+=c+2
            return total
        return dfs(0,-1) 