class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hash=Counter(answers)
        rabbits=0
        for x in hash:
            rabbits+=ceil(hash[x]/(x+1))*(x+1)
        return rabbits