class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        s = ""
        nums = num
        num = str(num)
        for i in range(len(num)):
            if len(s) == k:
                if int(s)!=0 and nums%int(s) == 0:
                    count+=1
                s = s[1:]+num[i]  
            else:
                s+=num[i]
        if int(s)!=0 and nums%int(s) == 0:
                    count+=1
        return count
            