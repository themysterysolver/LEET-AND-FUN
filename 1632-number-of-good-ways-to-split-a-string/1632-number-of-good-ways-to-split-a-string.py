class Solution:
    def numSplits(self, s: str) -> int:
        left = [0]*len(s)
        right = [0]*len(s)
        c = set()
        for i in range(len(s)):
            if not c:
                c.add(s[i])
                left[i] += 1
            elif s[i] in c:
                left[i] = left[i-1]
            else:
                left[i] = left[i-1]+1
                c.add(s[i])
        c =set()
        for i in range(len(s)-1,-1,-1):
            if not c:
                c.add(s[i])
                right[i] += 1 
            elif s[i] in c:
                right[i] = right[i+1]
            else:
                right[i] = right[i+1] + 1
                c.add(s[i])
        print(left)
        print(right)
        count = 0
        for i in range(len(left)-1):
            if left[i] == right[i+1]:
                count += 1
        return count
