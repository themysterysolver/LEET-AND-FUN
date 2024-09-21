#time limit exceeds!
class Solution:
    def removeStars(self, s: str) -> str:
        count=s.count("*")
        s=list(s)
        print(count)
        if '*' not in s:
            return ''.join(s)
        while count!=0:
            index_first=s.index("*")
            s[:]=s[:index_first-1]+s[index_first+1:]
            count-=1
        return ''.join(s)
