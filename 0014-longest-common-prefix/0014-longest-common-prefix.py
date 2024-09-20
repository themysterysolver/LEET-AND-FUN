class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        print(strs)
        strs.sort(key=lambda x:len(x))
        print(strs)
        base_case=strs[0]
        if len(base_case)==0:
            return ""
        for i in range(1,len(strs[0])+1):
            checker=base_case[:i]
            for j in strs:
                if checker!=j[:i]:
                    return base_case[:i-1]
        return base_case
            
            
    
        