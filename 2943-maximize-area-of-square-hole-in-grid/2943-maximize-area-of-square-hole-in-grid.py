class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def count_it(nums):
            nums.sort()
            streak = 1
            maxi = 1
            for i in range(1,len(nums)):
                if nums[i]-nums[i-1] == 1:
                    streak+=1
                    print(streak)
                else:
                    maxi = max(maxi,streak)
                    streak = 1
            maxi = max(maxi,streak)
            #print(nums,maxi+1)
            return maxi+1
        return min(count_it(hBars),count_it(vBars))**2
                    
