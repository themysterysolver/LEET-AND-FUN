class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        left=[0]*n
        right=[0]*n
        force=0
        for i in range(n):
            if dominoes[i]=='R':
                force=n
                right[i]=force
            elif dominoes[i]=='L':
                force=0
                right[i]=force
            else:
                force-=1
                right[i]=max(0,force)
        print(right)
        force=0
        for i in range(n-1,-1,-1):
            if dominoes[i]=='L':
                force=n
                left[i]=force
            elif dominoes[i]=='R':
                force=0
                left[i]=force
            else:
                force-=1
                left[i]=max(0,force)
        print(left)
        ans=""
        for i in range(n):
            a=right[i]-left[i]
            if a>0:
                ans+='R'
            elif a<0:
                ans+='L'
            else:
                ans+='.'
        return ans

