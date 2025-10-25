class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        mini = float('inf')
        for ch in "balon":
            if ch in ['l','o']:
                mini = min(mini,c[ch]//2)
            else:
                mini = min(mini,c[ch])
        return mini if mini!=float('inf') else 0