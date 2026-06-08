#vamsi my boi goat!
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        hash = defaultdict(list)
        for idx,c in enumerate(ring):
            hash[c].append(idx)
        # print(hash)
        @cache
        def go(idx,i):
            if i == m:
                return 0
            if ring[idx] == key[i]:
                return 1+go(idx,i+1)
            mini = float('inf')
            for next in hash[key[i]]:
                g = go(next,i)
                cost = min(abs(next-idx),abs(n-abs(next-idx)))
                mini = min(cost+g,mini)
            return mini
        return go(0,0)
        

