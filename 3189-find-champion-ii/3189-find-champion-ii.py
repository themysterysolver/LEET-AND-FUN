class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        championExist=[False]*n
        for start,end in edges:
            championExist[end]=True
        if championExist.count(False)>1:
            return -1
        else:
            return championExist.index(False)
