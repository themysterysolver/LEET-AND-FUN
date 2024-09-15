class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat)==1:
            return mat[0][0]
        if len(mat)==2:
            return mat[0][0]+mat[1][1]+mat[0][1]+mat[1][0]
        else:
            sum_diagonal=0
            for i in range(len(mat)):
                if i==len(mat)//2 and len(mat)%2==1:
                    sum_diagonal+=mat[i][i]
                else:
                    sum_diagonal+=mat[i][i]+mat[i][len(mat)-i-1]
            return sum_diagonal
        