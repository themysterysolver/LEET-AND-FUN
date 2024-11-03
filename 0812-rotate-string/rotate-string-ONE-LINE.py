class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        return True if goal in s+s and len(s)==len(goal) else False     
