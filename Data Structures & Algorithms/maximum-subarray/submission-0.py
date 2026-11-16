class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # R: The question is asking us to find the subarray with the largest sum and we need to return the sum.
        # E: What if the array is empty?. What if the array 
        # A: My approach to this problem would be to have varribales maxSum and currSum. MaxSum would hold the value of nums[0] while currSum would hold the value of 0. i would then make sure that currSum is a positive number by getting the max of itself and 0. This is handy becasue when we come accross a negative number that brings our currSum down we can fallback to the max. i will repeat this process till i get ther maxSum and return it. the time complexity for this is O(n)
        # C:

        maxSum = nums[0] 
        currSum = 0     

        for n in nums:    
            currSum = max(currSum, 0) 
            currSum += n   
            maxSum = max(maxSum, currSum)
        return maxSum
            
