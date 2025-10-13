class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        stack = []
        for w in words:
            if stack and sorted(stack[-1]) == sorted(w):
                continue
            else:
                stack.append(w)
        return stack