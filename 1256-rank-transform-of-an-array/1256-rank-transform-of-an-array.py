class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_pos=arr[:]
        rank_pos=list(set(rank_pos))
        d=dict()
        rank_pos.sort()
        for i in range(len(rank_pos)):
            d[rank_pos[i]]=i+1
        rank=[]
        for i in range(len(arr)):
            rank.append(d[arr[i]])
        return rank
        