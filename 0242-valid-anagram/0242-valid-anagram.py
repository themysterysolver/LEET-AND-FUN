class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        print s
        print t
        if s==t:
            return True
        return False


        