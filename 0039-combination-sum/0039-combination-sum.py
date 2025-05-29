class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(sumx,path):
            if sumx>target:
                return
            if sumx==target:
                #print(path,path.split('.'),path.split('.')[1:],tuple(map(int,path.split('.')[1:])))
                result.append(list(map(int,path.split('.')[1:])))
            for i in range(len(candidates)):
                backtrack(sumx+candidates[i],path+"."+str(candidates[i]))
        backtrack(0,"")
        for r in result:
            r.sort()
        return list(set(map(tuple,result)))