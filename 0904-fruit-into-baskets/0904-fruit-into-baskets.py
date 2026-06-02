class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxi = float('-inf')
        left = 0
        s = set()
        hash = defaultdict(int)
        for r in range(len(fruits)):
            s.add(fruits[r])
            hash[fruits[r]]+=1
            while len(s)>2:
                hash[fruits[left]]-=1
                if hash[fruits[left]] == 0:
                    s.remove(fruits[left])
                left+=1
            maxi = max(maxi,r-left+1)
        return maxi