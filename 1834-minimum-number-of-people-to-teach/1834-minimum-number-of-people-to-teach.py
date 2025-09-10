class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        hash = defaultdict(set)
        for user,lang in enumerate(languages):
            for l in lang:
                hash[user+1].add(l)
        
        probs = set()
        for u1,u2 in friendships:
            if len(hash[u1] & hash[u2])>0:
                continue
            else:
                probs.add(u1)
                probs.add(u2)
        
        if not probs:
            return 0
        
        p = list(probs)
        mini = float('inf')
        for l in range(1,n+1):
            count = 0
            for el in p:
                if l not in hash[el]:
                    count += 1
            mini = min(mini,count)
        return mini