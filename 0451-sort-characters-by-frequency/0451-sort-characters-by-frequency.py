class Solution:
    def frequencySort(self, s: str) -> str:
        hash=dict()
        for c in s:
            hash[c]=hash.get(c,0)+1
        print(hash)
        listItems=list(hash.items())
        print(listItems)
        listItems.sort(key=lambda x:x[1],reverse=True)
        print(listItems)
        newS=""
        for c,n in listItems:
            newS+=c*n
        print(newS)
        return newS
