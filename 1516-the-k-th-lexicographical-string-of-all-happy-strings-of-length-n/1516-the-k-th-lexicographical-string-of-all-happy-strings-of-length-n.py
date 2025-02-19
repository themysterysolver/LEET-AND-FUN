class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result=[]
        def backtrack(s):
            if len(s)==n:
                result.append(s)
                return
            for c in "abc":
                if not s or s[-1]!=c:
                    backtrack(s+c)
                    if len(result)==k:
                        return
        backtrack("")
        print(result)
        if len(result)==k:
            return result[-1]
        else:
            return ""