class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[i for i in range(1,n+1)]
        #print(arr)
        q=deque(arr)
        temp=k
        #print(len(q)>1,len(q))
        while len(q)>1:
            temp-=1
            next=q.popleft()
            if temp==0:
                temp=k
            else:
                q.append(next)
        print(q)
        return q[0]
            
