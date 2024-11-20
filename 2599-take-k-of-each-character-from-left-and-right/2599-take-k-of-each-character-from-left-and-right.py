#https://www.youtube.com/watch?v=3Y_0LagNMxM
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq={'a':0,'b':0,'c':0}
        for i in s:
            freq[i]+=1
        print(freq)
        for key,val in freq.items():
            if val<k:
                return -1
        window=[0]*3
        left,window_max=0,0
        for right in range(len(s)):
            window[ord(s[right])-ord('a')]+=1
            while left<=right and (freq['a']-window[0]<k or freq['b']-window[1]<k or freq['c']-window[2]<k):
                window[ord(s[left])-ord('a')]-= 1
                left+=1
            window_max=max(window_max,right-left+1)
        return len(s)-window_max