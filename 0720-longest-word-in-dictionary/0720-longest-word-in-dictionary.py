class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        s = set()
        s.add("")
        for w in words:
            if w[:-1] in s:
                s.add(w)
        print(s)  
        l = 0
        maxi = "Z"*10
        for w in sorted(list(s)):
            if len(w)>l:
                print("He")
                l = len(w)
                maxi = max(maxi,w)
        return maxi if maxi!="Z"*10 else ""