class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for p in paths:
            s = p.split()
            path = s[0]
            for el in s[1:]:
                idx = el.index('(')
                hash[el[idx+1:-1]].append(path+'/'+el[:idx])
        #print(hash)
        return [val for val in hash.values() if len(val)>1]