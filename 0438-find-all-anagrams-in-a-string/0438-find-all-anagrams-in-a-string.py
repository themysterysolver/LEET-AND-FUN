class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        c=Counter(p)
        window_size=len(p)
        result=[]
        hash=defaultdict(int)
        start=0
        for i in range(len(s)):
            if i-start>=window_size:
                if hash==c:
                    result.append(start)
                hash[s[start]]-=1
                if hash[s[start]]==0:
                    del hash[s[start]]
                start+=1
                hash[s[i]]+=1
            else:
                hash[s[i]]+=1
            #print(i,list(hash.items()),start)
        if hash==c:
            result.append(start)
        return result