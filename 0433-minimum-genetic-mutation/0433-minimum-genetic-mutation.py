#respect to WORD LADDER 124
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        word_pattern = defaultdict(list)
        pattern_word = defaultdict(list)
        
        bank.append(startGene)

        for word in bank:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                word_pattern[word].append(pattern)
                pattern_word[pattern].append(word)
        
        q = deque([startGene])
        visited = {startGene}
        count = 0
        print(word_pattern)
        print(pattern_word)
        while q:
            l = len(q)
            for _ in range(l):
                word = q.popleft()
                if word == endGene:
                    return count
                for pat in word_pattern[word]:
                    for w in pattern_word[pat]:
                        if w not in visited:
                            q.append(w)
                            visited.add(w)
            count+=1
        return -1

