class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        if len(chars)==1:
            return 1
        count=0
        stri=""
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                count=count+1
            else:
                count=count+1
                if count==1:
                    stri=stri+chars[i]
                else:
                    stri=stri+chars[i]+''.join(list(str(count)))
                count=0
            print i,stri,count
        if chars[-2]==chars[-1]:
            count=count+1
            if count==1:
                stri=stri+chars[-1]
            else:
                stri=stri+chars[-1]+''.join(list(str(count)))
        else:
            stri=stri+chars[-1]
        chars[:]=stri[:]
        return len(chars)