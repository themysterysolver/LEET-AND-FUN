# using heap to find always the shortest path my always being greedy and choosing the smallest vaue to reach the end.Example2 give u a spark how to solve
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        n=len(grid)
        heap=[(grid[0][0],0,0)]
        t=0
        visited=set()
        visited.add((0,0))
        while heap:
            time,x,y=heapq.heappop(heap)
            t=max(t,time)
            if (x,y)==(n-1,n-1):
                return t
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if nx<0 or nx>=n or ny<0 or ny>=n or (nx,ny) in visited:
                    continue
                else:
                    heapq.heappush(heap,(grid[nx][ny],nx,ny))
                    visited.add((nx,ny))
        return -1