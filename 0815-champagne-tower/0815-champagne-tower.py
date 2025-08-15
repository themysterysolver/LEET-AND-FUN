class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # def display(g):
        #     for row in g:
        #         print(g)
        #     print('------------------')
        g = [[0.0]*101 for _ in range(101)]
        # display(g)
        
        g[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r + 1):
                if g[r][c] > 1:
                    ex = g[r][c] - 1.0
                    g[r][c] = 1
                    g[r+1][c] += ex/2
                    g[r+1][c+1] += ex/2                     
                
        return g[query_row][query_glass]