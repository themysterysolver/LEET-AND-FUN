class TrieNode:
    def __init__(self):
        self.child=[None]*26
        self.end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()    
    def insert(self, word: str) -> None:
        current=self.root
        for c in word:
            idx=ord(c)-ord('a')
            if current.child[idx]:
                current=current.child[idx]
            else:
                newNode=TrieNode()
                current.child[idx]=newNode
                current=current.child[idx]
        current.end=True
    def search(self, word: str) -> bool:
        current=self.root
        for c in word:
            idx=ord(c)-ord('a')
            if not current.child[idx]:
                return False
            current=current.child[idx]
        if current.end==True:
            return True
        else:
            return False
    def startsWith(self, prefix: str) -> bool:
        current=self.root
        for c in prefix:
            idx=ord(c)-ord('a')
            if not current.child[idx]:
                return False
            current=current.child[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)