class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=s.split()
        print a
        l=len(a)-1
        return len(a[l])

        