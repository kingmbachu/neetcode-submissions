class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        current = []
        def dfs(i,  total):
            if total == target:
                output.append(current.copy())
                return

            if total > target:
                return 

            if i == len(nums):
                return

            current.append(nums[i])
            dfs(i, total + nums[i])
            current.pop()

            dfs(i+1, total)

        dfs(0,0)
        return output
  

 
 


