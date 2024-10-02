class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_pos=arr[:]
        print(rank_pos)
        rank_pos=list(set(rank_pos))
        rank_pos.sort()
        print(rank_pos)
        rank=[]
        for i in arr:
            rank.append(rank_pos.index(i)+1)
        return rank
        
