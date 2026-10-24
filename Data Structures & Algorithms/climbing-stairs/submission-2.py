class Solution:
    def climbStairs(self, n: int) -> int:
        
        # This is our handle case. so incase our n is one of these numbers we return 1 or 2. And from here we can build our dp table. The next step here we are creating our table that will contain n+1 0's. The reason why  its n+1 is because the indexes contain the number of steps and holds the value which is the number of ways. Step 3: We then give the values of 1 and 2 to their respective indexes which is 1 and 2. remember that 0 is unused because we are not using it in this question hence why we start at number on n as 1 or 2.
        if n == 1 or n == 2:
            return n 
        
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2


        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[i]



        
