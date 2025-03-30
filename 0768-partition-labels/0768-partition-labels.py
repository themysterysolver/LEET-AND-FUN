class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result=[]
        hash=Counter(s)
        count=0
        encountered=set()
        for i in range(len(s)):
            if i!=0 and len(encountered)==0:
                result.append(count)
                count=0
            count+=1
            encountered.add(s[i])
            hash[s[i]]-=1
            if hash[s[i]]==0:
                encountered.remove(s[i])
        result.append(count)
        return result
            