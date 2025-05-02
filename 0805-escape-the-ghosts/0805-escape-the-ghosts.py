class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        player_distance=abs(target[0])+abs(target[1])
        min_dist=float('inf')
        for x,y in ghosts:
            min_dist=min(min_dist,(abs(x-target[0])+abs(y-target[1])))
        return True if player_distance<min_dist else False