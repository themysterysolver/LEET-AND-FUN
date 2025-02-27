class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        maxi=0
        nset=set(arr)
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                prev=arr[j]
                curr=prev+arr[i]
                count=2
                while curr in nset:
                    count+=1
                    prev,curr=curr,curr+prev
                    maxi=max(count,maxi)
        return maxi
                    

            