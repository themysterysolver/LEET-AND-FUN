class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)<3:
            return len(s)
        hash=Counter(s)
        count=0
        print(hash)
        for key,val in hash.items():
            if val%2==1:
                count+=val-1
            else:
                count+=val-2
        print(count)
        return len(s)-count
        