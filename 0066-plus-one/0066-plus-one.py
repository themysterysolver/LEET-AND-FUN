class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in range(len(digits)):
           num=num*10+digits[i]
        num=num+1
        print num
        b=[]
        while num!=0:
            temp=num%10
            b.insert(0,temp)
            num=num/10
        print b
        digits[:]=b[:]
        return b


        