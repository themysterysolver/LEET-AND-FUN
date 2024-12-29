class TrieNode:
    def __init__(self):
        self.child=[None]*26
        self.end=False
class WordDictionary:
    def __init__(self):
        self.root=TrieNode()
    def addWord(self, word: str) -> None:
        current=self.root
        for s in word:
            idx=ord(s)-ord('a')
            if current.child[idx]:
                current=current.child[idx]
            else:
                newNode=TrieNode()
                current.child[idx]=newNode
                current=current.child[idx]
        current.end=True
    def search(self, word: str) -> bool:
        def dfs(root,idx):
            if idx==len(word):
                return root.end
            if word[idx]=='.':
                for children in root.child:
                    if children and dfs(children,idx+1):
                        return True
            else:
                nidx=ord(word[idx])-ord('a')
                if root.child[nidx]:
                    return dfs(root.child[nidx],idx+1)
            return False
        return dfs(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)