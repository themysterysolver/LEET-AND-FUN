class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adV={i:[] for i in range(n)}
        hasDestination=[False]*n
        for start,end in edges:
            hasDestination[end]=True
            adV[start].append(end)
        print(adV)
        result=[]
        for i in range(len(hasDestination)):
            if hasDestination[i]==False:
                result.append(i)
        return result