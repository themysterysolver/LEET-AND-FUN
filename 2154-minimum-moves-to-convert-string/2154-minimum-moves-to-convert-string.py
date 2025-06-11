#after seeing an 'X' we default move 2char space without,here it simply works if u work it down deeply
class Solution:
    def minimumMoves(self, s: str) -> int:
        if 'X' not in s:
            return 0
        if '0' not in s and set(s)=={'X'}:
            print(len(s)/3)
            return math.ceil(len(s)/3)
        count=0
        i=0
        while i<len(s):
            if s[i]=='X':
                count+=1
                i+=2
            i+=1
        return count