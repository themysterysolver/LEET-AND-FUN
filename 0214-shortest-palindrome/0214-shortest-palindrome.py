class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        idx = 0
        for i in range(len(s)):
            if s[:i] == s[:i][::-1]:
                idx = i
        print(idx)
        return s[idx:][::-1]+s
         


































        # s = s+'#'+s[::-1]
        # n = len(s)
        # lps = [0]*n
        # i = 1
        # length = 0
        # while i<n:
        #     if s[i] == s[length]:
        #         length += 1
        #         lps[i] = length
        #         i += 1
        #     else:
        #         if length != 0:
        #             length = lps[length-1]
        #         else:
        #             lps[i] = 0
        #             i += 1
        # return s[lps[-1]:]
