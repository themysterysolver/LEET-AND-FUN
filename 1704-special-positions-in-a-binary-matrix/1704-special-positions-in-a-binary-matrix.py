class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row=[0]*len(mat)
        col=[0]*len(mat[0])

        for i,r in enumerate(mat):
            row[i]=r.count(1)
        #print(row)

        for i in range(len(mat[0])):
            for j in range(len(mat)):
                if mat[j][i]==1:
                    col[i]+=1
        #print(col)   
        count=0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                #print(i,j,row[i],col[j],row[i]==1 and col[j]==1)
                if row[i]==1 and col[j]==1 and mat[i][j]==1:
                    count+=1
        return count
