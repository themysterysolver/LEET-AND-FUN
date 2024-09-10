class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0 for _ in range(n)] for _ in range(n)]
        count=0
        print(matrix)
        left,top=0,0
        right,bottom=len(matrix)-1,len(matrix)-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                matrix[top][i]=count+1
                count+=1
            top+=1
            for i in range(top,bottom+1):
                matrix[i][right]=count+1
                count+=1
            right-=1
            for i in range(right,left-1,-1):
                matrix[bottom][i]=count+1
                count+=1
            bottom-=1
            for i in range(bottom,top-1,-1):
                matrix[i][left]=count+1
                count+=1
            left+=1
        return matrix
        