#use hahsmap, even odd sum diff order parity
#goated prabha instincts
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hash=defaultdict(list)
        r,c=len(mat),len(mat[0])
        for i in range(r):
            for j in range(c):
                hash[i+j].append(mat[i][j])
        h=list(hash.items())
        h.sort()
        #print(h)
        result=[]
        for k,val in h:
            if k&1!=1: #even
                result+=val[::-1]
            else:
                result+=val
        return result