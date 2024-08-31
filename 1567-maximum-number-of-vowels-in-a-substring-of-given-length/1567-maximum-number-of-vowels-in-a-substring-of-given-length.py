class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """ 
        start=0
        vowel=0
        count=0
        for i in range(len(s)):
            if((i-start)%k==0 and i!=0):
                if(s[start] in 'aeiou'):
                    vowel=vowel-1
                start=start+1
            if(s[i] in 'aeiou'):
                vowel=vowel+1
            print i,s[i],vowel,start,s[start]
            count=max(vowel,count)
        return count

                

            
            

        
            
                
        