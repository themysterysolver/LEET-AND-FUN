class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        state=[['.']*n for _ in range(n)]
        res=[]
        visited_col=set()
        visited_da=set()#diagonal
        visited_ad=set()#antidiagonal
        def backtrack(r):
            if r==n:
                res.append([''.join(row) for row in state])
                return 
            for c in range(n):
                diff=r-c
                sumi=r+c
                if not(c in visited_col or diff in visited_da or sumi in visited_ad):       
                    visited_col.add(c)
                    visited_ad.add(sumi)
                    visited_da.add(diff)
                    state[r][c]='Q'
                    backtrack(r+1)

                    visited_col.remove(c)
                    visited_ad.remove(sumi)
                    visited_da.remove(diff)
                    state[r][c]='.'
        backtrack(0)
        return res

