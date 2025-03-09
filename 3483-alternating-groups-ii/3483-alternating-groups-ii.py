class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors+=[colors[i] for i in range(k-1)]
        n=len(colors)
        left,right=0,1
        count=0
        while right<n:
            if colors[right]==colors[right-1]:
                left=right
                right+=1
                continue
            right+=1
            if right-left<k:
                continue
            count+=1
            left+=1
        return count
            
            
