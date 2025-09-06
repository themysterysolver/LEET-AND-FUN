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

    def startsWith(self,word):
        count = 0
        current = self.root
        for w in word:
            if w in current.child:
                count+=1
                current = current.child[w]
            else:
                return count
        return count
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(str,arr1))
        arr2 = list(map(str,arr2))

        myTrie = Trie()
        for w in arr2:
            myTrie.__insert__(w)
        
        maxi = 0
        for w in arr1:
            maxi=max(maxi,myTrie.startsWith(w))
        return maxi