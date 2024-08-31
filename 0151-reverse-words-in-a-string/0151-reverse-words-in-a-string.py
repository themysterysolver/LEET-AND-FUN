class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        print (s)
        a=""
        stack=[]
        count=1
        for i in s:
            if not i.isspace():
                a=a+i
                count=0
            if i.isspace() and count==0:
                if not a.isspace():
                    stack.append(a)
                    stack.append(' ')
                a=""
                count=1
            #print stack
        if a:
            stack.append(a)
        if stack and stack[-1].isspace():
            stack.pop()
        #print ("STACK:",stack)
        rev=""
        while(len(stack)!=0):
            rev=rev+stack.pop()
        print stack
        print rev
        return rev
        