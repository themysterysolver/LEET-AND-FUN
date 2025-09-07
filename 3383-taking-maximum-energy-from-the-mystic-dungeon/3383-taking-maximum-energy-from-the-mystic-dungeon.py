class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [e for e in energy]
        n = len(energy)
        for i in range(len(energy)-1,-1,-1):
            if i+k<n:
                dp[i] = dp[i+k]+energy[i]
        return max(dp)