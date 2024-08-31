class Solution:
    def findComplement(self, num: int) -> int:
        blength=num.bit_length()
        print (blength)
        c=(1<<blength)-1
        return (num^c)

        