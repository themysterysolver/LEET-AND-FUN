class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        listx=nums[:n]
        listy=nums[n:]
        print(listx,listy)
        ans=[]
        for i in range(n):
            ans.append(listx[i])
            ans.append(listy[i])
        return ans