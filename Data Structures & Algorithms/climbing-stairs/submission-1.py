class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1 or n == 2:
            return n

        prev = 1
        curr = 2

        for stair in range(3, n + 1):
            nextWays = prev + curr
            prev = curr
            curr = nextWays
        return curr