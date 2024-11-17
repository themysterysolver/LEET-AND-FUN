class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adV={i:[] for i in range(1,n+1)}
        for start,end in trust:
            adV[start].append(end)
        print(adV)
        for key,val in adV.items():
            if len(val)==0:
                flag=True
                for keyn,valn in adV.items():
                    if keyn==key:
                        continue
                    if key in valn:
                        continue
                    else:
                        flag=False
                if flag:
                    return key
        return -1