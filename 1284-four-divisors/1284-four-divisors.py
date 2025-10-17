class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # @cache
        # def divisors(n):
        #     count = 2
        #     ans = [1,n]
        #     for i in range(2,int(math.sqrt(n))+1):
        #         if n%i == 0 and n//i!=i:
        #             ans.append(i)
        #             ans.append(n//i)
        #             count+=2
        #             if count>4:
        #                 return (False,[])
        #     #print(n,count,ans)
        #     return (count == 4,ans)
        sumx = 0
        for n in nums:
            d = set()
            count = 0
            for i in range(1,int(math.sqrt(n))+1):
                if n%i == 0:
                    d.add(i)
                    d.add(n//i)
  
                    if len(d)>4:
                        break
            if len(d) == 4:
                sumx+=sum(d)
            #print(n,count,d)
        return sumx