class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        s = SortedList([])
        print(s)
        start = 0
        ans = []
        for r in range(len(nums)):
            if r-start<k:
                s.add(nums[r])
            else:
                if k%2 == 1:
                    ans.append(s[k//2])
                else:
                    ans.append((s[k//2]+s[k//2-1])/2)
                s.add(nums[r])
                s.discard(nums[start])
                start+=1
            # print(s)
        if k%2 == 1:
            ans.append(s[k//2])
        else:
            ans.append((s[k//2]+s[k//2-1])/2)
        return ans