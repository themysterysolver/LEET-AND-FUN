class Solution:
    def largestDivisibleSubset(self, nums):
        # Step 1: Sort the numbers so that divisors come before their multiples
        nums.sort()
        n = len(nums)

        # dp[i] will hold the size of the largest divisible subset ending with nums[i]
        dp = [1] * n

        # Variables to track the size and ending index of the maximum subset
        max_size = 1
        max_index = 0

        # Step 2: Fill the dp array using nested loops
        for i in range(1, n):
            for j in range(i):
                # If nums[i] is divisible by nums[j], it can be chained to the subset ending at nums[j]
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1

            # Update the largest subset info if we found a longer one
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        # Step 3: Reconstruct the subset by walking backward from max_index
        result = []
        current_num = nums[max_index]
        current_size = max_size

        for i in range(max_index, -1, -1):
            # If the current number is divisible and matches the expected size
            if current_num % nums[i] == 0 and dp[i] == current_size:
                result.append(nums[i])
                current_num = nums[i]
                current_size -= 1

        # Since we collected elements in reverse order, reverse to return in ascending order
        result.reverse()
        return result