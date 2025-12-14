class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        def vowel(x):
            count = 0
            for c in x:
                if c in "aeiou":
                    count+=1
            return count
        first = vowel(arr[0])
        ans = arr[0]
        for i in range(1,len(arr)):
            if vowel(arr[i])==first:
                ans+=" "+arr[i][::-1]
            else:
                ans+=" "+arr[i]
        return ans