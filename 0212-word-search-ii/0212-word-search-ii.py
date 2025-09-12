class TrieNode:
    def __init__(self):
        self.child = dict()
        self.end = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def __insert__(self,word):
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr = curr.child[w]
        curr.end = True
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        myTrie = Trie()
        for w in words:
            myTrie.__insert__(w)
        

        res = set()
        row,col = len(board),len(board[0])
        
        def dfs(i,j,curr):
            if i<0 or j<0 or i>=row or j>=col:
                return
            w = board[i][j]
            
            if w in curr.child:
                curr = curr.child[w]
                if curr.end:
                    res.add(curr.word)
                temp,board[i][j] = board[i][j],'#'
                dfs(i,j+1,curr)
                dfs(i+1,j,curr)
                dfs(i-1,j,curr)
                dfs(i,j-1,curr)
                board[i][j] = temp
                
        
        curr = myTrie.root
        for i in range(row):
            for j in range(col):
                dfs(i,j,curr)
        
        return list(res)
