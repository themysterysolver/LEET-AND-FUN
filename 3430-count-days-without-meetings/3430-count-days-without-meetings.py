class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        #print(meetings)
        merged=[]
        for x,y in meetings:
            if not merged:
                merged.append([x,y])
            else:
                if x<=merged[-1][-1]:
                    if y>merged[-1][-1]:
                        merged[-1][-1]=y
                else:
                    merged.append([x,y])
        #print(merged)
        for x,y in merged:
            days-=(y-x+1)
        return days