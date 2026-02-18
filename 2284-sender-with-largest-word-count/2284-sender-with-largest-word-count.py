class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        hash = defaultdict(list)
        for i in range(len(messages)):
            hash[senders[i]].append(messages[i])
        maxi = 0
        name = ""
        for key,val in hash.items():
            k = 0
            for v in val:
                k+= len(v.split())
            if k>maxi: 
                maxi = k
                name = key
            if k == maxi:
                if key>name:
                    name = key
            #print(key,v,maxi,name)
        return name