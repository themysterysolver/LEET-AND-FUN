class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def swap(state,i,j):
            state=list(state)
            state[i],state[j]=state[j],state[i]
            return ''.join(state)
        directions=[[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
        visited=set()
        finalState="123450"
        startState=""
        for i in range(len(board)):
            for j in range(len(board[0])):
                startState+=str(board[i][j])
        print(startState)
        q=deque([startState])
        moves=0
        while q:
            l=len(q)
            for _ in range(l):
                currState=q.popleft()
                if currState==finalState:
                    return moves
                zeroIdx=currState.index("0")
                for newIdx in directions[zeroIdx]:
                    nextState=swap(currState,zeroIdx,newIdx)
                    if nextState in visited:
                        continue
                    q.append(nextState)
                    visited.add(nextState)
            moves+=1
        return -1
        