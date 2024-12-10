class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        count=0
        end=intervals[0][1]
        for x,y in intervals[1:]:
            if x<end:
                count+=1
                end=min(end,y)
            else:
                end=y
        return count