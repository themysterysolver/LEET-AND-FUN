class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance)<0:
            return -1
        idx = -1
        for i,num in enumerate(balance):
            if num<0:
                idx = i
        if idx == -1:
            return 0
        l = len(balance)
        def bfs(idx):
            sumx = balance[idx]
            left,right = (idx-1)%l,(idx+1)%l
            ld,rd = 1,1
            cost = 0
            while sumx!=0:
                if ld<rd:
                    wanted = min(balance[left],-1*sumx)
                    sumx+=wanted
                    cost+=wanted*ld
                    left=(left-1)%l
                    ld+=1
                elif ld>rd:
                    wanted = min(balance[right],-1*sumx)
                    sumx+=wanted
                    cost+=wanted*rd
                    right=(right+1)%l
                    rd+=1
                else:
                    if balance[left]>balance[right]:
                        wanted = min(balance[left],-1*sumx)
                        sumx+=wanted
                        cost+=wanted*ld
                        left=(left-1)%l
                        ld+=1 
                    else:
                        wanted = min(balance[right],-1*sumx)
                        sumx+=wanted
                        cost+=wanted*rd
                        right=(right+1)%l
                        rd+=1
            return cost
        return bfs(idx)
        