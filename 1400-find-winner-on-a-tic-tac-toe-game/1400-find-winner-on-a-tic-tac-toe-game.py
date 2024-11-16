class Solution:
    def checker(self,space):
        prob=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for x,y,z in prob:
            if space[x] and space[x]==space[y] and space[y]==space[z]:
                return space[x]
        return None
    def tictactoe(self, moves: List[List[int]]) -> str:
       space=[None]*9
       print(space)
       for i in range(len(moves)):
            r,c=moves[i]
            pt=(r*3)+c
            if i%2==0:
                space[pt]='A'
            else:
                space[pt]='B'
            ch=self.checker(space)
            print(space)
            if ch==None:
                continue
            else:
                return ch
       return "Draw" if len(moves)==9 else "Pending"


        