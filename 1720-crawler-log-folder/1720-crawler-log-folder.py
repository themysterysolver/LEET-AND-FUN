class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for s in logs:
            if s=="./":
                pass
            elif s=="../":
                if count>0:
                    count-=1
            else:
                count+=1
        return count