class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        res = re.fullmatch(p,s)
        if res == None:
            return False
        return True