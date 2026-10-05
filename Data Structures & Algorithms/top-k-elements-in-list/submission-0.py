class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        for number in nums:
            if number not in seen:
                seen[number] = 1
            else:
                seen[number] += 1
            # seen = {"1:1", "2:2", "3:4"}

        buckets = [[] for _ in range(len(nums) + 1)]
         # nums = [5, 5, 5, 5, 5] len = 5 freq = 5
         # bucket = [[] [] [] [] [] [5]]
        for number, frequency in seen.items():
            buckets[frequency].append(number)
    #This line basically goes to the frequency in buckets  
    # and adds the number to that frquency (index)
        answer = []
        for bucket in reversed(buckets):
            for number in bucket:
                answer.append(number)

            if len(answer) == k:
                return answer
        #This makes sense because we want the length of answer to be the same length of k eg. k = 2, therefore our list should contain 2 elements in the list.


   