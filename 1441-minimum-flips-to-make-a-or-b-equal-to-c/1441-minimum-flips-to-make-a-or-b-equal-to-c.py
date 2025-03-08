class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        maxi=max(a.bit_length(),b.bit_length(),c.bit_length())
        a,b,c=bin(a)[2:].zfill(maxi),bin(b)[2:].zfill(maxi),bin(c)[2:].zfill(maxi)
        print(a,b,c)
        count=0
        for i in range(maxi):
            if int(a[i])|int(b[i])!=int(c[i]):
                if c[i]=="1":
                    count+=1
                else:
                    count+=[a[i],b[i]].count("1")
        return count