class Solution:
    def intToRoman(self, num: int) -> str:
        ones=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hundereds=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thousand=["","M","MM","MMM"]
        return thousand[num//1000]+hundereds[(num%1000)//100]+tens[(num%100)//10]+ones[(num%10)]