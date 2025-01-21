class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n1=list(bin(x)[2:])
        n2=list(bin(y)[2:])
        print('{},{}'.format(n1,n2))
        if len(n1)<len(n2):
            n1=['0']*(len(n2)-len(n1))+n1
        else:
            n2=['0']*(len(n1)-len(n2))+n2
        print('{},\n,{}'.format(n1,n2))
        count=0
        for i in range(len(n1)):
            if n1[i]!=n2[i]:
                count+=1
        return count