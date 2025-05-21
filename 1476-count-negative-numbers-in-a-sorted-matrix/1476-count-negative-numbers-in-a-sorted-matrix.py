class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def display(mat):
            for row in mat:
                print(row)
            print('-------')
        #display(grid)
        count=0
        row,col=len(grid)-1,0
        while row>=0 and col<len(grid[0]):
            if grid[row][col]<0:
                count+=len(grid[row])-col
                row-=1
            else:
                col+=1
        return count