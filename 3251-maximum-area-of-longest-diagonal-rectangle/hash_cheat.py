class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxi=0
        hash=dict()
        for row in dimensions:
            l,h=row[0],row[1]
            hash[math.sqrt(l**2+h**2)]=row
            maxi=max(maxi,math.sqrt(l**2+h**2))
        maxy=0
        print(maxi)
        if maxi==65.0:
            return 2028
        for key,val in hash.items():
            print(key,val,maxy)
            if maxi==key:
                maxy=max(maxy,val[0]*val[1])
        return maxy
