class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        row,col = len(grid),len(grid[0])
        prefix = [0]*(row*col)
        sufix = [0]*(row*col)
        product = [0]*(row*col)
        
        
        for i in range(row):
            for j in range(col):
                idx = i*col+j
                if i==0 and j==0:
                    prefix[idx] = grid[i][j] %12345
                else:
                    prefix[idx] = grid[i][j]*(prefix[(idx)-1]) %12345


        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                idx = i*col+j
                if i==row-1 and j==col-1:
                    sufix[idx] = grid[i][j] %12345
                else:
                    sufix[idx] = grid[i][j]*(sufix[(idx)+1]) %12345

        for i in range(row):
            for j in range(col):
                idx  = i*col+j
                if i==0 and j==0:
                    product[idx] = sufix[(idx)+1] %12345
                elif i==row-1 and j==col-1:
                    product[idx] = prefix[(idx)-1] % 12345
                else:
                    prod = sufix[(idx)+1]*prefix[(idx)-1] %12345
                    product[idx] = prod

        #print(prefix)
        #print(sufix)   
        #print(product) 

        result = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                result[i][j] = product[i*col+j]
        
        return result