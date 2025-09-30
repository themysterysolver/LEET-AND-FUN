class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        i = p.index('*')
        p = p[:i]+'.*'+p[i+1:]
        return bool(re.search(p,s))
        
            
        