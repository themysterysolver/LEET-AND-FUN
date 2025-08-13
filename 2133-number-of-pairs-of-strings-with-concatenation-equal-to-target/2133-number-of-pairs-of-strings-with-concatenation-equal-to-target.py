class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        c= Counter(nums)
        keys = c.keys()
        ans = 0
        print(keys)
        for key in keys:
            if target.startswith(key):
                print(key)
                l = len(key)
                rem = target[l:]
                if rem in keys and rem!=key:
                    ans += (c[key]*c[rem])
                if rem == key:
                    ans += c[key]*(c[key]-1)
        return ans