class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        #why can't I go from reverse?
        count = 0
        while target!=1:
            if target%2 != 0:
                target-=1
            elif target%2 == 0 and maxDoubles>0:
                target//=2
                maxDoubles-=1
            else:
                if maxDoubles == 0:
                    count+=target-2
                    target = 1
                else:
                    target-=1
            count+=1
        return count