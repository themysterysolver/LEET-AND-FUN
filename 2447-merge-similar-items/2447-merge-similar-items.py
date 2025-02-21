class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hash=defaultdict(int)
        for key,val in items1:
            hash[key]+=val
        for key,val in items2:
            hash[key]+=val
        a=list(map(list,hash.items()))
        a.sort(key=lambda x:x[0])
        return a