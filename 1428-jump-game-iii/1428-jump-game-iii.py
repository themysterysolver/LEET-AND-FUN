#dp method-just recursion with cach help
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        l=len(arr)
        visited=set()
        @cache
        def go(idx):
            if idx>=l or idx<0 or idx in visited:
                return False
            if arr[idx]==0:
                return True
            visited.add(idx)
            return go(idx+arr[idx]) or go(idx-arr[idx])
        return go(start)