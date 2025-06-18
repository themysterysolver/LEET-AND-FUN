#dp with recursion just rereading the prob statement,just remeber the -ve edges case scenario
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stoness=set(stones)

        @cache
        def jump(idx,k):
            if idx==stones[-1]:
                return True
            if idx>stones[-1] or k<=0:
                return False
            if idx in stoness:
                return jump(idx+k+1,k+1) or jump(idx+k-1,k-1) or jump(idx+k,k)
            return False
        return jump(1,1)