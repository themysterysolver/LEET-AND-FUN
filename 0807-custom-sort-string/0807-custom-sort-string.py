class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq=Counter(s)
        #print(freq)
        permuted=""
        for i in order:
            if i in freq:
                permuted+=i*freq[i]
        #print(permuted)
        for key in freq.keys():
            if key not in set(order):
                permuted+=key*freq[key]
        #print(permuted)
        return permuted