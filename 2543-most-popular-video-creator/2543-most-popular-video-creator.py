class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        cToId = defaultdict(list) #creators to Id
        cToV = defaultdict(int) #creators ti View count

        for i in range(len(ids)):
            heapq.heappush(cToId[creators[i]],(views[i]*-1,ids[i]))
            cToV[creators[i]]+=views[i]
        
        maxi = max(cToV.values())
        ans = []
        for key,val in cToV.items():
            if val == maxi:
                x,y = heapq.heappop(cToId[key])
                ans.append([key,y])
        return ans
