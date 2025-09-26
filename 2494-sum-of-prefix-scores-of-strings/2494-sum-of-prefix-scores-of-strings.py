class TrieNode:
    def __init__(self):
        self.parent = dict()
        self.counter = defaultdict(int)
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        r = self.root
        for w in word:
            if w not in r.parent:
                r.parent[w] = TrieNode()
            r.counter[w] += 1
            r = r.parent[w]
        r.end = True

    def countIt(self,word):
        count = 0
        curr = self.root
        for w in word:
            if w in curr.parent:
                count+=curr.counter[w]
                # if curr.end:
                #     break
                curr = curr.parent[w]
            else:
                break 
        return count

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t = Trie()
        for w in words:
            t.insert(w)
        ans = []
        for w in words:
            ans.append(t.countIt(w))
        return ans