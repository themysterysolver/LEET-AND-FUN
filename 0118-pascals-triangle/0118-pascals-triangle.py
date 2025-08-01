class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p=[]
        if numRows>=1:
            p.append([1])

        for i in range(1,numRows):
            new=[1]
            #print(i,len(p[-1]),p[-1])
            for j in range(1,len(p[-1])):
                #print(p[-1][j-1],p[-1][j],j)
                new.append(p[-1][j-1]+p[-1][j])
            new.append(1)
            #print(new)
            #print('--------------')
            p.append(new)
        return p
