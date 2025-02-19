class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result=[]
        def backtrack(c,s):
            result.append(''.join(c))
            for i in range(len(s)):
                c.append(s[i])
                backtrack(c,s[:i]+s[i+1:])
                c.pop()
        backtrack([],tiles)
        print(result)
        return len(set(result))-1