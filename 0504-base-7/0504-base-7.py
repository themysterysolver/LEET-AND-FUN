class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        flag=False
        if num<0:
            flag=True
            num=(-num)
        string=""
        while(num>0):
            string=str(num%7)+string
            num=num//7
        if flag:
            string="-"+string
        return string