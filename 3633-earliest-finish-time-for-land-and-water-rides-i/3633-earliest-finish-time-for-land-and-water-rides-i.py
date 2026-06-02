class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        mini = float('inf')
        for lst,ld in zip(landStartTime,landDuration):
            time = lst+ld
            mint = float('inf')
            for wst,wd in zip(waterStartTime,waterDuration):
                if wst<=time:
                    mint = min(wd,mint)
                else:
                    mini = min(mini,time+(wst-time)+wd)
            mini = min(mint+time,mini)
        for lst,ld in zip(waterStartTime,waterDuration):
            time = lst+ld
            mint = float('inf')
            for wst,wd in zip(landStartTime,landDuration):
                if wst<=time:
                    mint = min(wd,mint)
                else:
                    mini = min(mini,time+(wst-time)+wd)
            mini = min(mint+time,mini)
        return mini