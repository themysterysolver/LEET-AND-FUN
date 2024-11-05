class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def display(mat):
            for row in mat:
                print(row)
            print('-----------------------')
        result=[]
        i,j=king
        board=[["."]*8 for _ in range(8)]
        board[i][j]="K"
        display(board)
        for r,c in queens:
            board[r][c]="Q"
        display(board)
        count=0
        #RIGHT
        for k in range(j+1,8):
            if board[i][k]=="Q":
                result.append([i,k])
                break
        #LEFT
        for k in range(j-1,-1,-1):
            if board[i][k]=="Q":
                result.append([i,k])
                break
        #DOWN
        for k in range(i+1,8):
            if board[k][j]=="Q":
                result.append([k,j])
                break
        #UP
        for k in range(i-1,-1,-1):
            if board[k][j]=="Q":
                result.append([k,j])
                break
        #RIGHT-UP
        temp=j
        for k in range(i-1,-1,-1):
            temp+=1
            if temp>=8:
                    break
            if board[k][temp]=="Q":
                result.append([k,temp])
                break
        #LEFT-DOWN
        temp=j
        for k in range(i+1,8):
            temp-=1
            if temp<0:
                    break
            if board[k][temp]=="Q":
                result.append([k,temp])
                break

        #LEFT-UP
        temp=j
        for k in range(i-1,-1,-1):
            temp-=1
            if temp<0:
                    break
            if board[k][temp]=="Q":
                result.append([k,temp])
                break
        #RIGHT-DOWN
        temp=j
        for k in range(i+1,8):
            temp+=1
            if temp>=8:
                    break
            if board[k][temp]=="Q":
                result.append([k,temp])
                break
        result.sort(key=lambda x:(x[0],x[1]))
        print(result)
        return result
