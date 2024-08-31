class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        d={5:0,10:0,20:0}
        for i in bills:
            if i in d:
                d[i]=d[i]+1
            print 'start:',i,d
            if i==5:
                continue
            elif i==10:
                if d[5]>=1:
                    d[5]=d[5]-1
                else:
                    return False
            elif i==20:
                if d[10]>=1 and d[5]>=1:
                    d[10]=d[10]-1
                    d[5]=d[5]-1
                elif d[5]>=3:
                    d[5]=d[5]-3
                else:
                    return False
            print 'end:',i,d
        return True
                
        