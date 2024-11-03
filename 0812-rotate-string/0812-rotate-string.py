class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(s)+1):
            if s[i:]+s[:i]==goal:
                return True
        return False     