class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                continue
            else:
                if i>0 and flowerbed[i-1]==1:
                    continue
                elif i<len(flowerbed)-1 and flowerbed[i+1]==1:
                    continue
                else:
                    flowerbed[i]=1
                    n-=1
                    if n==0:
                        break
            #print(i,flowerbed,n)
        return True if n==0 else False