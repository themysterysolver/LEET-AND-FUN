class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        a=matrix
        row=[]
        column=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    row.append(i)
                    column.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row:
                    matrix[i][j]=0
            for j in column:
                matrix[i][j]=0
        return matrix
            
        
                
        