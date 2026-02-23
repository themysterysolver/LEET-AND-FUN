class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        setter = set()
        for i in range(len(s)-k+1):
            setter.add(s[i:i+k])
        print(setter)
        return len(setter) == 2**k