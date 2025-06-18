class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def display(mat):
            for key,val in mat.items():
                print(key,val)
            print('-----')
        if endWord not in wordList:
            return 0
        word_to_pattern=defaultdict(list)
        pattern_to_word=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pat=word[:i]+"*"+word[i+1:]
                word_to_pattern[word].append(pat)
                pattern_to_word[pat].append(word)
        #display(word_to_pattern)
        #display(pattern_to_word)
        count=0
        q=deque([beginWord])
        visited={beginWord}
        while q:
            l=len(q)
            for _ in range(l):
                word=q.popleft()
                if word==endWord:
                    return count+1
                for pat in word_to_pattern[word]:
                    for w in pattern_to_word[pat]:
                        if w not in visited:
                            q.append(w)
                            visited.add(w)
            count+=1
            #print(q,count)
        return 0