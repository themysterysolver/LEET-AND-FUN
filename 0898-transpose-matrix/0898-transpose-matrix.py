class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        a=[]
        for i in range(len(matrix[0])):
            mat=[]
            for j in range(len(matrix)):
                mat.append(matrix[j][i])
            a.append(mat)
        return a
        