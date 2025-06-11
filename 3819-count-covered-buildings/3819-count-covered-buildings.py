# checkiing and storing only min and max for each x to it's y and vice versa
# x stores y's min and max
#y stores x's min and max
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x=defaultdict(list)
        y=defaultdict(list)
        for u,v in buildings:
            if u not in x:
                x[u]=[v,v]
            else:
                x[u][0]=min(x[u][0],v)
                x[u][1]=max(x[u][1],v)
            if v not in y:
                y[v]=[u,u]
            else:
                y[v][0]=min(y[v][0],u)
                y[v][1]=max(y[v][1],u)
        # print(x)
        # print(y)
        count=0
        for u,v in buildings:
            if x[u][0] < v < x[u][1] and y[v][0] < u < y[v][1]:
                count+=1 
        return count