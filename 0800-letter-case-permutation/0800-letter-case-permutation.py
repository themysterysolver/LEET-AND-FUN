class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result=[]
        def backtrack(i,w):
            if i==len(s):
                result.append(w)
                return
            if s[i].isdigit():
                backtrack(i+1,w+s[i])
            else:
                if s[i].isupper():
                    backtrack(i+1,w+s[i])
                    backtrack(i+1,w+s[i].lower())
                else:
                    backtrack(i+1,w+s[i])
                    backtrack(i+1,w+s[i].upper())
        backtrack(0,"")
        return result