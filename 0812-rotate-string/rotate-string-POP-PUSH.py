class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        l=list(s)
        g=list(goal)
        n=len(s)
        print (l)
        while(n!=0):
            l.append(l.pop(0))
            print (l)
            if l==g:
                return True
            n-=1
        return False
