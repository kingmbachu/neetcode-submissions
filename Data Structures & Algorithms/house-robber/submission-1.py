class Solution:
    def rob(self, nums: List[int]) -> int:
        # R: The question is asking us to return the MAXIMUM amount of money without alerting the police. How do we alert the police? By robbing from either i-1 or i + 1 house. so essentially we can rob from any other house but not houses that are adjacent to i.
        # E: i) We can't rob from i -1 or i + 1. ii) if theres only 3 numbers in nums then return the ith number iii) what if theres only 2 numbers in the array or even one number?
        # A: My approach: skip = dp[i - 1], rob = nums[i] + dp[i - 2]


        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]