class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        def backtrack(idx,sumx,path,l):
            if idx==10 or sumx>n or l>k:
                return
            if sumx==n and len(path)==k:
                result.append(path[:])
                return
            for i in range(idx+1,10):
                backtrack(i,sumx+i,path+[i],1+1)
        for i in range(1,10):
            backtrack(i,i,[i],1)
        #print(result)
        return result