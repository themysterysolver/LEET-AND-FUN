class Solution:
    def myAtoi(self, s: str) -> int:
        s=re.findall("^[\ ]*([\+\-]?\d+)",s)
        if not s:
            return 0
        s=s[0]#converting list of string to string!
        i,sign=0,1# to check if 1st char has sign or not! i-->is the place from which we should start our evaluvation!!
        if s[0]=='-':
            i=1
            sign=-1
        elif s[0]=='+':
            i=1
        resnum=0
        for ch in s[i:]:
            resnum=resnum*10+ord(ch)-ord('0')
        return max(min(resnum*sign,2**31-1),-2**31)