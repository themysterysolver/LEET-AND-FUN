class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        count=0
        for i in range(8):
            for j in range(8):
                if board[i][j]=="R":
                    #RIGHT
                    for k in range(j+1,8):
                        if board[i][k]=="B":
                            break
                        elif board[i][k]=="p":
                            count+=1
                            break
                    #LEFT
                    for k in range(j-1,-1,-1):
                        if board[i][k]=="B":
                            break
                        elif board[i][k]=="p":
                            count+=1
                            break
                    #UP
                    for k in range(i-1,-1,-1):
                        if board[k][j]=="B":
                            break
                        elif board[k][j]=="p":
                            count+=1
                            break 
                    #DOWN
                    for k in range(i+1,8):
                        if board[k][j]=="B":
                            break
                        elif board[k][j]=="p":
                            count+=1
                            break 
                    break
        return count