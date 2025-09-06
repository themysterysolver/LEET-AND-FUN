class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.insert(0,0)
        horizontalCuts.append(h)
        verticalCuts.insert(0,0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        hmaxi = 0
        for i in range(len(horizontalCuts)-1):
            hmaxi = max(hmaxi,horizontalCuts[i+1]-horizontalCuts[i])
            # print(i,hmaxi)
        # print('-------------')
        vmaxi = 0
        for i in range(len(verticalCuts)-1):
            vmaxi = max(vmaxi,verticalCuts[i+1]-verticalCuts[i])
            # print(i,vmaxi)
        # print(vmaxi,hmaxi)
        return (vmaxi*hmaxi)%(10**9+7)