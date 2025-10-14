class TrieNode:
    def __init__(self):
        self.parent = dict()
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        self.curr = self.root
        for w in word:
            if w not in self.curr.parent:
                self.curr.parent[w] = TrieNode()
            self.curr = self.curr.parent[w]
        self.curr.end = True

    def endsWith(self,word):
        self.curr = self.root
        for w in word:
            if w in self.curr.parent:
                self.curr = self.curr.parent[w]
            else:
                break
        return len(self.curr.parent)>0


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        t = Trie()
        for w in words:
            t.insert(w[::-1])
        count = 0
        for w in words:
            if t.endsWith(w[::-1]):
                continue
            else:
                count+=len(w)+1
        return count
        

