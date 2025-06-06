class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans=[]
        for idx,(time,inc) in enumerate(customers):
            if idx==0:
                curr=time
                timeTook=curr+inc
                ans.append(timeTook-curr)
                curr=timeTook
            else:
                if time<curr:
                    timeTook=curr+inc
                    ans.append(timeTook-time)
                    curr=timeTook
                else:
                    curr=time
                    timeTook=curr+inc
                    ans.append(timeTook-curr)
                    curr=timeTook
            #print(ans)
        return sum(ans)/len(ans)