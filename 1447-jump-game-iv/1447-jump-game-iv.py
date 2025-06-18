# literal BFS as per prob statement on the adj ones and it's neighbours
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        adL=defaultdict(list)
        num=defaultdict(list)
        l=len(arr)
        for i in range(l):
            if i==0:
                adL[i].append(i+1)
            elif i==l-1:
                adL[i].append(i-1)
            else:
                adL[i].append(i+1)
                adL[i+1].append(i)
            num[arr[i]].append(i)
        q=deque([0])
        count=0
        visited=set()
        visited.add(0)
        while q:
            m=len(q)
            #print(q)
            for _ in range(m):
                node=q.popleft()
                if node==l-1:
                    return count
                for el in adL[node]:
                    if el not in visited:
                        q.append(el)
                        visited.add(el)
                for idx in num[arr[node]]:
                    if idx!=node:
                        q.append(idx)
                        visited.add(idx)
                num[arr[node]].clear()
            count+=1
        return -1