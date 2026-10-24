class Solution:
    def climbStairs(self, n: int) -> int:
        
        # This is our handle case. so incase our n is one of these numbers we return 1 or 2. And from here we can build our dp table. The next step here we are creating our table that will contain n+1 0's. The reason why  its n+1 is because the indexes contain the number of steps and holds the value which is the number of ways. Step 3: We then give the values of 1 and 2 to their respective indexes which is 1 and 2. remember that 0 is unused because we are not using it in this question hence why we start at number on n as 1 or 2. Step 3: We want to now iterate over the number we are looking for so we create a for loop right. And we start at 3 and end at n + 1, because we want to make sure we are getting the iterations from 3 till the last number so we can always add them up. Then we use the formula dp[i] = dp[i - 1] + dp[i -2]. This is simply the recurrence formula. We then return the dp[i] whiich will be our value for whatever n is. DP= Dynamic programming. The time complexity for this is O(n) as we are iterating through the dp list once. Space Complexity is O(n)
        if n == 1 or n == 2:
            return n 
        
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2


        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[i]



        
