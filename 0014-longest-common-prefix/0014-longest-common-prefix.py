## divergence is the logic!
## Trie
class TrieNode:
    def __init__(self):
        self.child = dict()
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def __insert__(self,word):
        current = self.root
        for w in word:
            if w not in current.child:
                current.child[w] = TrieNode()
            current = current.child[w]
        current.end = True
    
    def LCP(self):
        ans = ''
        current = self.root
        while True:
            if len(current.child)==1 and not current.end:
                key = next(iter(current.child))
                ans+=key
                current = current.child[key]
            else:
                break
        return ans
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
            myTrie = Trie()
            for w in strs:
                myTrie.__insert__(w)
            
            return myTrie.LCP()
            
    
        