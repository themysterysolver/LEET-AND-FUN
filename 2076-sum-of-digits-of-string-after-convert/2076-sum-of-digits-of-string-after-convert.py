class Solution:
    def getLucky(self, s: str, k: int) -> int:
        '''this=""
        #a=list(map(str,map(ord,s)))
        for i in a:
            this=this+i'''
        a = [str(ord(char) - 96) for char in s]
        this = "".join(a)
        this=int(this)
        print(a,this,type(this))
        this=int(this)
        print(this,type(this))
        sumi=0
        while this!=0:
            sumi=sumi+this%10
            this=this//10
            if this==0:
                print(sumi)
                k=k-1
                if k==0:
                    return sumi
                else:
                    this=sumi
                    sumi=0
