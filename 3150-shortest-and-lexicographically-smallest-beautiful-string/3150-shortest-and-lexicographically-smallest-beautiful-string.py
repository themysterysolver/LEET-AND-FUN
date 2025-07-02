class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        candidate=""
        res=""
        left = 0
        countOnes = 0
        for right in range(len(s)):
            if s[right]=="1":
                countOnes+=1
            while countOnes>k:
                if s[left]=="1":
                    countOnes-=1
                left+=1
            if countOnes==k:
                while left<right and s[left]=="0":
                    left+=1
                candidate=s[left:right+1]
                if res=="" or len(candidate)<len(res) or len(candidate)==len(res) and candidate<res:
                    res=candidate
        return res