class TrieNode:
    def __init__(self):
        self.parent = dict()
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        curr = self.root
        for w in word:
            if w not in curr.parent:
                curr.parent[w] = TrieNode()
            curr = curr.parent[w]
        curr.end = True
    
    def suffix(self,word):
        curr = self.root
        for w in word:
            if w in curr.parent:
                curr = curr.parent[w]
                if curr.end:
                    return True
            else:
                return False
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = ""
        for w in words:
            self.trie.insert(w[::-1])

    def query(self, letter: str) -> bool:
        self.stream+=letter
        return self.trie.suffix(self.stream[::-1])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)