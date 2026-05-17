class TrieNode:
    def __init__(self):
        self.child = [0]*26
        self.le = float('inf')
        self.end = False
        self.idx = float('inf')

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def build(self,word,l,i):
        root = self.root
        # self.l = l
        # self.idx = i
        for c in word:
            idx = ord(c)-ord('a')
            if root.child[idx]==0:
                root.child[idx] = TrieNode()
            root = root.child[idx]
            if l<=root.le:
                if l == root.le:
                    root.idx = min(root.idx,i)
                else:
                    root.le = l
                    root.idx = i
        root.end = True
        if l<=root.le:
            if l == root.le:
                root.idx = min(root.idx,i)
            else:
                root.le = l
                root.idx = i


    def cusSearch(self,w):
        root = self.root
        
        for i,c in enumerate(w):
            idx = ord(c)-ord('a')
            #print(idx,c)
            if root.child[idx] == 0:
                if i !=0:
                    return root.idx
                else:
                    return -1
            root = root.child[idx]
        return root.idx

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        
        t = Trie()
        mini = float('inf')
        minindex = 0
        for idx,w in enumerate(wordsContainer):
            t.build(w[::-1],len(w),idx)
            if len(w)<mini:
                mini = len(w)
                minindex = idx
        ans = []
        for w in wordsQuery:
            a = t.cusSearch(w[::-1])
            #print('---------')
            ans.append(a if a!=-1 else minindex)
        return ans
        
        