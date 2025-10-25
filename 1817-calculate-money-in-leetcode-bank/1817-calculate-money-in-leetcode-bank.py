class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        monday = 0
        while n>0:
            for i in range(1,8):
                money+=(monday+i)
                n-=1
                if n == 0:
                    break
            if n == 0:
                break
            monday+=1
        return money
            