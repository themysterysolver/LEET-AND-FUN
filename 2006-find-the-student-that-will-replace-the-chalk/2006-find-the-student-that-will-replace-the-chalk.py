class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sumi=sum(chalk)
        k=k%sumi
        print(k,sumi,chalk)
        for i in range(len(chalk)):
            if k<chalk[i]:
                return i
            k=k-chalk[i]
        

