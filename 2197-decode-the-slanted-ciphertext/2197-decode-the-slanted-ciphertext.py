# construct a matrix
# then diag traversal
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        def display(matrix):
            for row in matrix:
                print(row)
            print('--------')
        s=encodedText
        # print(rows,len(s))
        r,c=rows,len(s)//rows
        mat=[['']*c for _ in range(r)]
        #display(mat)
        k=0
        for i in range(r):
            for j in range(c):
                mat[i][j]=s[k]
                k+=1
        #display(mat)
        hash=defaultdict(list)
        for i in range(r):
            for j in range(c):
                hash[j-i].append(mat[i][j])
        h=list(hash.items())
        h.sort()
        # print(h)
        result=""
        for k,val in h:
            if k>-1:
                result+=''.join(val)
        # print(result)
        result=result.rstrip()  #result=result.lstrip().rstrip()
        # print(result)
        return result