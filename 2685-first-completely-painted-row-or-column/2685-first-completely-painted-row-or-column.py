class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        def display(mat):
            for row in mat:
                print(row)
            print('-----------')
        row,col=len(mat),len(mat[0])
        hash=dict()
        for i in range(row):
            for j in range(col):
                hash[mat[i][j]]=(i,j)
        #print('Initial hash:',hash)
        #display(mat)
        rowHash={i:0 for i in range(row)}
        colHash={i:0 for i in range(col)}
        #print(rowHash,colHash)
        for i in range(len(arr)):
            x,y=hash[arr[i]]
            rowHash[x]+=1
            colHash[y]+=1
            #print(x,y,i,rowHash,colHash,rowHash[x],colHash[y])
            if rowHash[x]==col or colHash[y]==row:
                return i
        return -1
