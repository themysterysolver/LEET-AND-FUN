class TrieNode:
    def __init__(self):
        self.parent = dict()
        self.end = False
        self.index = -1
        self.isPal = []
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.res = []

    def insert(self,word,idx):
        curr = self.root
        for i,c in enumerate(word):
            #doing it in prev(the current curr) so it becomes next
            if word[i:] == word[i:][::-1]:
                #print(i,word[i:],word[i::][::-1])
                curr.isPal.append(idx)
            if c not in curr.parent:
                curr.parent[c] = TrieNode()
            #curr.index.append(idx)
            curr = curr.parent[c]
        curr.end = True
        curr.index = idx
        #curr.isPal.append(idx)

    def isThere(self,word,idx):
        curr = self.root
        #print(word)
        for index,w in enumerate(word):
            if curr.end and word[index:] == word[index:][::-1]:
                self.res.append([idx,curr.index]) 
            if w in curr.parent:
                curr = curr.parent[w]
            else:
                return []
        if curr.end and curr.index!=idx:
            self.res.append([curr.index,idx])

        for p in curr.isPal:
            if p!=idx:
                self.res.append([idx,p])
        
        


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        t = Trie()
        for idx,word in enumerate(words):
            t.insert(word[::-1],idx)
        result = []
        for i,w in enumerate(words):
            x = t.isThere(w,i)
            
        return t.res