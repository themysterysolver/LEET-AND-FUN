class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if len(set(tops))==1 or len(set(bottoms))==1:
            return 0
        c1=Counter(tops)
        c2=Counter(bottoms)
        h1=[(-val,key) for key,val in c1.items()]
        h2=[(-val,key) for key,val in c2.items()]
        heapq.heapify(h1)
        heapq.heapify(h2)
        print(h1[0])
        print(h2[0])
        _,m1=h1[0]
        count1=0
        for i in range(len(tops)):
            if tops[i]!=m1:
                if bottoms[i]==m1:
                    count1+=1
                else:
                    count1=0
                    break
        print(count1)
        
        _,m2=h2[0]
        count2=0
        for i in range(len(bottoms)):
            if bottoms[i]!=m2:
                if tops[i]==m2:
                    count2+=1
                else:
                    count2=0
                    break
        print(count2)

        if count1>0 and count2>0:
            return min(count1,count2)
        elif count1>0:
            return count1
        elif count2>0:
            return count2
        else:
            return -1
            
