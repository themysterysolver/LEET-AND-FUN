class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        c=candidates
        l,r=c,len(costs)-c-1
        n=len(costs)
        #costs=list((val,idx) for idx,val in enumerate(costs))
        leftHeap,rightHeap=[(costs[i],i) for i in range(c)],[(costs[i],i) for i in range(n-c,n)]
        heapq.heapify(leftHeap)
        heapq.heapify(rightHeap)
        #print(list(enumerate(costs)))
        #print('l:',l,'r:',r,'c[l]:',costs[l][r]:',costs[r])
        #print(leftHeap,rightHeap)
        money=0
        while k!=0:
            x1,y1=leftHeap[0] if leftHeap else (float('inf'), float('inf'))
            x2,y2=rightHeap[0] if rightHeap else (float('inf'), float('inf'))
            if x1<x2:
                m,_=heapq.heappop(leftHeap)
                money+=m
                if l<=r and l<n:
                    heapq.heappush(leftHeap,(costs[l],l))
                    l+=1
            elif x1>x2:
                m,_=heapq.heappop(rightHeap)
                money+=m
                if l<=r and l<n:
                    heapq.heappush(rightHeap,(costs[r],r))
                    r-=1
            else:
                if y1<y2:
                    m,_=heapq.heappop(leftHeap)
                    money+=m
                    if l<=r and l<n:
                        heapq.heappush(leftHeap,(costs[l],l))
                        l+=1
                elif y1>y2:
                    m,_=heapq.heappop(rightHeap)
                    money+=m
                    if l<=r and l<n:  
                        heapq.heappush(rightHeap,(costs[r],r))
                        r-=1
                else:
                    m,_=heapq.heappop(rightHeap)
                    m1,_=heapq.heappop(leftHeap)
                    money+=m
                    if l<=r and l<n:  
                        heapq.heappush(rightHeap,(costs[r],r))
                        r-=1
                    if l<=r and l<n:
                        heapq.heappush(leftHeap,(costs[l],l))
                        l+=1
            k-=1
        print(money)
        return money


        
