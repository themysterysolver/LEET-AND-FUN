#instead of finding suffix to prefix ,we can do prefix to suffix
#eliminating common words for each prefix then multiplying it by 2 would be super good!
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        hash = defaultdict(set)
        for idea in ideas:
            hash[ord(idea[0])-ord('a')].add(idea[1:])
        count = 0
        for i in range(26):
            if len(hash[i])>0:
                for j in range(i+1,26):
                    if len(hash[j])>0:
                        common = len(hash[i]&hash[j])
                        count+=2*(len(hash[i])-common)*(len(hash[j])-common)
        return count