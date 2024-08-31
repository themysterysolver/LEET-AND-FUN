class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        l=['(','{','[']
        r=[')','}',']']
        for i in s:
            if i in l:
                stack.append(i)
            elif i in r:
                if(len(stack)>0):
                    check=stack.pop()
                else:
                    return 0
                    sys.exit(1)
                    break
                if  i=='}' and check=='{':
                    continue
                elif  i==']' and check=='[':
                    continue
                elif i==')' and check=='(':
                    continue
                else:
                    return 0
        if(len(stack)==0):
            return 1
        else:
            return 0

        