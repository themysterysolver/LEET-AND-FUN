class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l=len(citations)
        left,right=0,l-1
        while left<=right:
            mid=(left+right)//2
            print('start',left,right,mid)
            if citations[mid]==l-mid:
                return l-mid
            elif citations[mid]<l-mid:
                left=mid+1
            else:
                right=mid-1
            print('end',left,right)
        return l-left