class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        print(skill)
        skill.sort()
        print(skill)
        result=[]
        for i in range(len(skill)//2):
            result.append((skill[i],skill[len(skill)-i-1]))
        print(result)
        resultant=[]
        for i in result:
            resultant.append(sum(i))
        if len(set(resultant))==1:
            ans=0
            for i in result:
                ans+=i[0]*i[1]
            return ans
        else:
            return -1