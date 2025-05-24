class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices=[]
        for idx,el in enumerate(words):
            if x in el:
                indices.append(idx)
        return indices