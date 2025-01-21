class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        openedPenalty=[0]*(n+1)
        closedPenalty=[0]*(n+1)
        for i in range(n):
            if customers[i]=='N':
                openedPenalty[i+1]=openedPenalty[i]+1
            else:
                openedPenalty[i+1]=openedPenalty[i]
        for i in range(n-1,-1,-1):
            if customers[i]=='Y':
                closedPenalty[i]=closedPenalty[i+1]+1
            else:
                closedPenalty[i]=closedPenalty[i+1]
        #print('{}\n{}'.format(openedPenalty,closedPenalty))
        mini=[float('inf'),float('inf')]
        for i in range(n+1):
            sumi=openedPenalty[i]+closedPenalty[i]
            if sumi<mini[0]:
                mini[0]=sumi
                mini[1]=i
        return mini[1]
                