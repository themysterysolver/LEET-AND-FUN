class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        #print(candidates)
        result=[]
        def backtrack(sumx,start,path):
            if sumx==0:
                result.append(path[:])
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>sumx:
                    break
                backtrack(sumx-candidates[i],i+1,path+[candidates[i]])
        backtrack(target,0,[])
        return result