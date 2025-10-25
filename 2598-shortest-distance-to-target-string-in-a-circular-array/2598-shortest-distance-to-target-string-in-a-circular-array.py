class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        l,r = startIndex,startIndex
        d = 0
        while True:
            if words[l] == target or words[r] == target:
                return d
            l = (l-1+len(words))%len(words)
            r = (r+1+len(words))%len(words)
            d+=1