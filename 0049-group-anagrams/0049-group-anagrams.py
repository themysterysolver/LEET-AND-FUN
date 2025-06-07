class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash=defaultdict(list)
        for c in strs:
            d=''.join(sorted(c))
            hash[d].append(c)
        return list(hash.values())