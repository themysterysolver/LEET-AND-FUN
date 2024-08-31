class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s
        if not s:
            return ""
        a=list(s)
        maxi=0
        f=[]
        left,right=0,0
        for i in range(len(a)):

            l,r=i,i
            #odd length,expanding from centre!
            while l>=0 and r<len(a) and a[l]==a[r]:
                    maxi=max(maxi,len(a[l:r+1]))
                    if maxi==len(a[l:r+1]):
                        f=a[l:r+1]
                    l=l-1
                    r=r+1
            #even length,expanding or starting stome i,i+1
            l,r=i,i+1
            while l>=0 and r<len(a) and a[l]==a[r]:
                    maxi=max(maxi,len(a[l:r+1]))
                    if maxi==len(a[l:r+1]):
                        f=a[l:r+1]
                    l=l-1
                    r=r+1
        return ''.join(f)           
            