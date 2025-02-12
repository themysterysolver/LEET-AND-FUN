class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def cal(number):
            return sum(map(int,str(number)))
        hash=defaultdict(list)
        for idx,num in enumerate(nums):
            hash[cal(num)].append(idx)
        print(hash)
        maxi=float('-inf')
        for key,val in hash.items():
            if len(val)>1:
                result=[]
                for r in val:
                    result.append(nums[r])
                result.sort(reverse=True)
                maxi=max(maxi,sum(result[0:2]))
            else:
                continue
        print(maxi)
        return maxi if maxi!=float('-inf') else -1

