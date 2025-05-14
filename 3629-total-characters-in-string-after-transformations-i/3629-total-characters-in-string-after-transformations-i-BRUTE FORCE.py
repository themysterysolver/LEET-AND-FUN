class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod=10**9+7
        for i in range(t):
            temp=""
            for i in s:
                if i!="z":
                    temp+=chr(ord(i)+1)
                else:
                    temp+="ab"
            #print(temp)
            s=temp
        return len(s)%mod
