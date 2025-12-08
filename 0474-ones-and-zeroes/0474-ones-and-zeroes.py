#pick and not pick dp!
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        @cache
        def countOZ(el):
            return [el.count('0') if '0' in el else 0,el.count('1') if '1' in el else 0]
        l = len(strs)

        #vamsi the goat!
        @cache
        def go(idx,M,N):
            if idx>=l:
                return 0
            x,y = countOZ(strs[idx])
            if x+M<=m and y+N<=n:
                return max(1+go(idx+1,x+M,y+N),go(idx+1,M,N))
            else:
                return go(idx+1,M,N)
        return go(0,0,0)