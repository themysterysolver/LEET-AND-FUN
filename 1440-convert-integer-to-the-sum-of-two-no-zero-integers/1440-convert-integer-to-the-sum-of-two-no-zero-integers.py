class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def isValid(num):
            #print(num)
            return '0' not in str(num)
        for i in range(1,n+1):
            if isValid(i) and isValid(n-i):
                return [i,n-i]
            
