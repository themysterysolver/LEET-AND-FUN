class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def disp(m):
            for r in m:
                print(r)
            print('-----------')
        disp(mat) 
        result=[]
        rev=True
        for i in range(len(mat[0])):
            diagonal=[]
            r,c=0,i
            while c>=0 and r<len(mat):
                diagonal.append(mat[r][c])
                r+=1
                c-=1
            if not rev:
                result.append(diagonal)
                rev=True
            else:
                result.append(diagonal[::-1])
                rev=False
        for i in range(1,len(mat)):
            diagonal=[]
            r,c=i,len(mat[0])-1
            while r<len(mat) and c>=0:
                diagonal.append(mat[r][c])
                r+=1
                c-=1
            if not rev:
                result.append(diagonal)
                rev=True
            else:
                result.append(diagonal[::-1])
                rev=False
        print(result)
        flat=[]
        for i in result:
            flat.extend(i)
        return flat
