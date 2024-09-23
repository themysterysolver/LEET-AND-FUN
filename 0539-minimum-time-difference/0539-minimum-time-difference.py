class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        print(timePoints)
        def givenToMinute(s):
            hrs=int(s[0:2])*60
            min=int(s[3:])+hrs
            return min
        new_time=[givenToMinute(num) for num in timePoints]
        print(new_time)
        min_time=float('inf')
        for i in range(1,len(new_time)):
            min_time=min(new_time[i]-new_time[i-1],min_time)
        min_time=min(min_time,givenToMinute("24:00")-(new_time[-1]-new_time[0]))
        return min_time