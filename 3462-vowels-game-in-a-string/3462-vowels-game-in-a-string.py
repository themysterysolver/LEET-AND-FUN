class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set(list("aeiou"))
        idx = []
        count = 0
        for i,num in enumerate(s):
            if num in vowels:
                idx.append(i)
                count+=1
        if count == 0:
            return False
        if count&1 == 1:
            return True
        else:
            return True
        