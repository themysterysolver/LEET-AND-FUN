class Solution:
    def numberToWords(self, num: int) -> str:
        nums=list(map(int,str(num)))
        print(nums)
        bten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        btwenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        bhundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        if num == 0:
            return "Zero"
        
        def convert(num):
            if num<10:
                return bten[num]
            if num<20:
                return btwenty[num%10]
            if num<100:
                return bhundred[num//10] + (" " + convert(num%10) if num%10!=0 else "")
            if num<1000:
                return convert(num//100) + " Hundred" + (" "+ convert(num%100) if num%100!=0 else "")
            if num<1000000: #for thousands
                return convert(num//1000) + " Thousand" + (" "+ convert(num%1000) if num%1000!=0 else "")
            if num<1000000000: #for million
                return convert(num//1000000) + " Million" + (" "+convert(num%1000000) if num%1000000!=0 else "")
            if num<1000000000000: #for billion
                return convert(num//1000000000) + " Billion" + (" "+ convert(num%1000000000) if num%1000000000!=0 else "")
        return convert(num)
