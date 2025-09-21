class Solution:
    def checkString(self, s: str) -> bool:
        return False if s.count('ba')>0 else True