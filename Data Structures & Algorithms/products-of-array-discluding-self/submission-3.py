class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # Create answer array
        answer = [1] * len(nums)

        # LEFT / PREFIX
        prefix = 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        # RIGHT / POSTFIX
        postfix = 1

        for i in reversed(range(len(nums))):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer