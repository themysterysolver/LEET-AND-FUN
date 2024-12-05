class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_','')!=target.replace('_',''):
            print(start.replace('_',''),target.replace('_',''))
            return False
        q1=[(i,start[i]) for i in range(len(start)) if start[i]!='_']
        q2=[(i,target[i]) for i in range(len(target)) if target[i]!='_']
        print(q1,'\n',q2)
        for i in range(len(q1)):
            sq1,c1=q1[i]
            sq2,c2=q2[i]
            if c1!=c2 or (c1=='L' and sq1<sq2) or (c1=='R'and sq1>sq2):
                return False
        return True