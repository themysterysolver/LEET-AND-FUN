class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sol=[]
        print(matrix)
        left=0
        top=0
        down=len(matrix)-1
        right=len(matrix[0])-1
        print("l r t d")
        while left<=right and top<=down:
            print(left,right,top,down)
            for i in range(left,right+1):
                sol.append(matrix[top][i])
            top+=1
            print(left,right,top,down)
            for i in range(top,down+1):
                sol.append(matrix[i][right])
            right-=1
            print(left,right,top,down)
            if not (left<=right and down>=top):
                break
            for i in range(right,left-1,-1):
                sol.append(matrix[down][i])
            down-=1
            print(left,right,top,down)
            for i in range(down,top-1,-1):
                sol.append(matrix[i][left])
            left+=1
            print(left,right,top,down)
            print("-------------------------")
        print(sol)
        
        return sol