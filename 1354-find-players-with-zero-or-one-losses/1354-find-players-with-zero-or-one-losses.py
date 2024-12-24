class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players=set()
        for x,y in matches:
            players.add(x)
            players.add(y)
        #print(players)
        hash={i:[0,0] for i in players}
        #print(hash)
        for x,y in matches:
            hash[x][0]+=1
            hash[y][1]+=1
        #print(hash)
        ans=[[],[]]
        for key,val in hash.items():
            w,l=val
            if l==0:
                ans[0].append(key)
            elif l==1:
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans
