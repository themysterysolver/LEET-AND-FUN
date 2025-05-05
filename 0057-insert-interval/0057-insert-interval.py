class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)
        merged=[]
        for x,y in intervals:
            if not merged:
                merged.append([x,y])
            if x<=merged[-1][-1]:
                if y>=merged[-1][-1]:
                    merged[-1][-1]=y
            else:
                merged.append([x,y])
        return merged

        
            