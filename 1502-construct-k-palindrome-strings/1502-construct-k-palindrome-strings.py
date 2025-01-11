class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        hash=Counter(s)
        print(hash)
        count=0
        for v in hash.values():
            if v%2==1:
                count+=1
        return True if count<=k else False
