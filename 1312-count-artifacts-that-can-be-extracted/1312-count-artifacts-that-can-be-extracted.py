class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        grid=[[0]*n for _ in range(n)]
        hash=dict()
        idx=0
        for x1,y1,x2,y2 in artifacts:
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    hash[(i,j)]=idx
            idx+=1
        for x,y in dig:
            hash[(x,y)]=-1
        #print(len(set(hash.values()))-1)
        return len(artifacts)-(len(set(hash.values()))-1)