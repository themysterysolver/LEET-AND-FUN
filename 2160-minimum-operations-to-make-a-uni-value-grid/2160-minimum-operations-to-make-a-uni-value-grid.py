class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        rem=set()
        straight=[]
        for row in grid:
            for i in row:
                rem.add(i%x)
                straight.append(i)
        #print(rem)
        straight.sort()
        #print(straight)
        if len(rem)>1:
            return -1
        median=straight[len(straight)//2]
        #print(median)
        count=0
        len(straight)
        for i in straight:
            count+=abs(median-i)//x
        return count