class Solution:
    def isValid(self, word: str) -> bool:
        return True if len(word)>=3 and word.isalnum() and re.search(r'[aeiouAEIOU]',word) and re.search(r'[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]',word) else False