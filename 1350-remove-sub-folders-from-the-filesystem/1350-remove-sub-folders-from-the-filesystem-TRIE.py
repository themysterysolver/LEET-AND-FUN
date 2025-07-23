class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,f):
        node = self.root
        for subf in f:
            if subf not in node.children:
                node.children[subf] = TrieNode()
            node = node.children[subf]
            if node.end:
                return False
        node.end = True
        return True
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = Trie()
        res = []
        for f in folder:
            paths = f.split('/')[1:]
            #print(paths)
            if trie.insert(paths):
                res.append(f)
        return res
