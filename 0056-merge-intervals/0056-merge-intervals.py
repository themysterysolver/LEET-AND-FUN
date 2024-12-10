class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        merged=[]
        for x,y in intervals:
            if not merged:
                merged.append([x,y])
            if x<=merged[-1][-1]:
                if y>merged[-1][-1]:
                    merged[-1][-1]=y
            else:
                merged.append([x,y])
        print(merged)
        return merged
