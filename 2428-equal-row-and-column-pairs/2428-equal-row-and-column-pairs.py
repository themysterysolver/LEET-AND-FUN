class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def display(mat):
            for row in mat:
                print(row)
            print('-------------------')
        transpose=[row[:] for row in grid]
        for i in range(len(transpose[0])):
            print('i',i)
            for j in range(0,i):
                print('j',j)
                transpose[i][j],transpose[j][i]=transpose[j][i],transpose[i][j]
        count=0
        display(grid)
        display(transpose)
        for row in grid:
            for col in transpose:
                if row==col:
                    count+=1
        return count