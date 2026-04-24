class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c = Counter(moves)
        return abs(c['R']-c['L'])+c['_']