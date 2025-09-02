class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        adL = defaultdict(list)
        hash = defaultdict(Counter)
        for u,v in edges:
            adL[u].append(v)
            adL[v].append(u)

        #print(adL)        

        def dfs(node,parent):
            if adL[node] == []:
                hash[node][labels[node]] = 1
                return hash[node]
            else:
                if labels[node] in hash[node]:
                    hash[node][labels[node]]+=1
                else:
                    hash[node][labels[node]]=1
                for el in adL[node]:
                    if el == parent:
                        continue
                    hash[node]+=dfs(el,node)
                return hash[node]
        dfs(0,-1)
        #print(hash)
        ans = [0]*n
        for i in range(n):
            ans[i] = hash[i][labels[i]]
        return ans
                
#lol got struck  at 4 [[0,2],[0,3],[1,2]] this test case and ssome dude at discusssion typed
# [[0,2],[0,3],[1,2]] is a valid test case because we are given an UNDIRECTED graph. The edge [1,2] does not necessarily mean that node 1 is the parent of 2, but that there exists an edge between them. So, the tree constructed would look like this:

#      0
#    /   \
#   3     2 
#          \
#           1
# hehee I did smartly keeeping my adL bi directional and parent to not go back...