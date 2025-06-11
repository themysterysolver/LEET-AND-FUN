class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxi=""
        for i,c in enumerate(number):
            if c==digit:
                maxi=max(maxi,number[:i]+number[i+1:])
        return maxi