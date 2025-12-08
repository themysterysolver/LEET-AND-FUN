class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0","1"]
        result = []
        def backtrack(l,s,count,prev):
            if l>n:
                return
            if  l == n and count>=1:
                result.append(s)
                return
            if not prev:
                backtrack(l+1,s+'1',count+1,True)
            else:
                backtrack(l+1,s+'0',count,False)
                backtrack(l+1,s+'1',count+1,True)
        backtrack(1,"0",0,False)
        backtrack(0,"",0,False)
        return result