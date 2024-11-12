class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def bs(target):
            left,right=0,len(items)-1
            maxi=0
            while left<=right:
                mid=(left+right)//2
                if items[mid][0]>target:
                    right=mid-1
                else:
                    maxi=max(maxi,items[mid][1])
                    left=mid+1
            return maxi
        items.sort(key=lambda x:(x[0],-x[1]))
        print(items)
        ans=[]
        maxi=items[0][1]
        ans=[]
        for i in range(len(items)):
            maxi=max(maxi,items[i][1])
            items[i][1]=maxi
        print(items)
        ans=[bs(q) for q in queries]
        return ans