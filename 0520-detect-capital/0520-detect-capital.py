class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allUpper=True
        for i in word:
            if i.isupper():
                continue
            else:
                allUpper=False
                break
        allLower=True
        for i in word:
            if i.islower():
                continue
            else:
                allLower=False
                break
        if word[0].isupper():
            fcaps=True
        else:
            fcaps=False
        for i in range(1,len(word)):
            if word[i].islower():
                continue
            else:
                fcaps=False
                break
        return fcaps or allLower or allUpper