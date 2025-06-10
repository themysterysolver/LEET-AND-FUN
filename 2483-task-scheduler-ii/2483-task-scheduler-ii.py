#the idea behind solving is to store the max days each time 
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        hash=dict()
        days=0
        for t in tasks:
            if t not in hash:
                days+=1
                hash[t]=days+1+space
            else:
                if hash[t]<=days:
                    days+=1
                    hash[t]=days+1+space
                else:
                    days=hash[t]
                    hash[t]=days+1+space
            #print(t,days,hash)
        return days