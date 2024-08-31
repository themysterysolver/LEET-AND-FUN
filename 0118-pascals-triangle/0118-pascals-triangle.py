class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        print numRows
        p=[]
        if numRows==1:
            p.append([1])
        if numRows==2 or numRows>2:
            p.append([1])
            p.append([1,1])
        i=0
        new=[1]
        for i in range(2,numRows):
            a=p.pop()
            p.append(a)
            for i in range(len(a)-1):
                new.append(a[i]+a[i+1])
            new.append(1)
            p.append(new)
            new=[1]
        return p



        