class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hash = defaultdict(int)
        for w,h in rectangles:
            ratio = w/h
            hash[ratio] += 1
        result  = 0
        for rect in hash.values():
            result += rect*(rect-1)//2
        return result