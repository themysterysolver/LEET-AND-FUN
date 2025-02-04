class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def display(matrix):
            for row in matrix:
                print(row)
            print('-------------------------')
        def check_count(s):
            print(s.count("X")-1==s.count("O") or s.count("X")==s.count("O"))
            return s.count("X")-1==s.count("O") or s.count("X")==s.count("O")
        def singleWin(s):
            seq=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,8]]
            count={"X":0,"O":0}
            for r in seq:
                x,y,z=r
                if s[x]!=" " and s[x]==s[y] and s[y]==s[z]:
                    count[s[x]]+=1
            print((count["X"]>=1 and count["O"]==0) or (count["O"]>=1 and count["X"]==0) or (count["O"]==0 and count["X"]==0))
            return (count["X"]>=1 and count["O"]==0 and s.count("X")-1==s.count("O")) or (count["O"]>=1 and count["X"]==0 and s.count("O")==s.count("X")) or (count["O"]==0 and count["X"]==0)
        s=""
        display(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                s+=board[i][j]
        return (check_count(s) and singleWin(s))
