class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adL=dict()
        print(adL)
        for idx,n in enumerate(edges):
            adL[idx]=n
        print(adL)
        fromNode1=[float('inf')]*len(edges)
        fromNode2=[float('inf')]*len(edges)
        #print(fromNode1,fromNode2)
        def BFS(node,fromNode):
            q=deque([node])
            count=1
            visited=set()
            visited.add(node)
            while q:
                n=q.popleft()
                if n==-1:
                    break
                fromNode[n]=count
                count+=1
                if adL[n] in visited:
                    continue
                q.append(adL[n])
                visited.add(adL[n])

        BFS(node1,fromNode1)
        BFS(node2,fromNode2)
        #print(fromNode1,fromNode2)
        fromNode1[node1]=0
        fromNode2[node2]=0
        mini=float('inf')
        idx=-1
        print(fromNode1)
        print(fromNode2)
        for i in range(len(edges)):
            sumx=max(fromNode1[i],fromNode2[i])
            if sumx<mini:
                mini=sumx
                idx=i
        return idx


        
        
        