class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        start = -1
        curr = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and start == -1:
                    start = i
                    curr = i
                if grid[i][j] == 1:
                    curr = i
        end = curr
        print(start,end)
        left = -1
        curr = -1
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == 1 and left == -1:
                    left = i
                    curr = i
                if grid[j][i] == 1:
                    curr = i
        right = curr
        return (end-start+1)*(right-left+1)