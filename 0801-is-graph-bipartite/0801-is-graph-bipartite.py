#A Bipartite graph can be imagined by giving alternate colours to all nodes,if we managed to do thatthen we can say it it bipartite.That is the the nodes of the graph can be seperated into 2 distinct set of vertices where no 2 vertices in a set are adjacent to each other!!
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adL={i:[] for i in range(len(graph))}
        color=[-1]*len(graph)
        for i in range(len(graph)):
            adL[i].extend(graph[i])
        print(adL)
        print(color)
        def BFS(adL):
            print('hello')
            for i in range(len(graph)):
                if color[i]==-1:
                    color[i]=0#Red
                    q=deque([i])
                    while q:
                        u=q.popleft()
                        for v in adL[u]:
                            if color[v]==-1:
                                color[v]=1-color[u]#providing alternate color than the one used for u!
                                q.append(v)
                            else:
                                if color[u]==color[v]:
                                    return False            
            return True
        return BFS(adL)