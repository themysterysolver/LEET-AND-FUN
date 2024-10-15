class Solution:                                  #Black-1 , White-0......Black to right and white to left!
    def minimumSteps(self, s: str) -> int:
        if '1' not in s or '0' not in s:
            return 0
        count=0
        prev_no_of_zeroes=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                count+=prev_no_of_zeroes
            elif s[i]=='0':
                prev_no_of_zeroes+=1
        return count
        