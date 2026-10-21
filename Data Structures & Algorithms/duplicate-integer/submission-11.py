class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
       ### "R =  The problem says given an array nums, we need to return true if there contains a duplicate number in the array."
       ## "E =  What if the nums array is empty?"
        #"A = My initial approach/ brute force approach is to have two nesteed loops where i starts at index 0 and j starts at i + 1. Then traverse through the list and return true if the number equals itself and false if we didnt find any number. The time complexity for that would be O(n^2) because we have two nested for loops and as the size n grows, so will the the the time too. space complexity is O(1) because we don't need to dynamically allocate memory anywhere. my optimal approach for this question would be using a hashset. we would first crewate a set and then go throuygh the nums array. we wiould check if the element is in the set first, if it isnt we add it to the set and the repeat the same processs, check if the element exists in the set if it doesnt we add , but if it does we return True immediataly. If we have looped through the set and we cant find any duplicate numebrs we return false. The time complexity for this is 0(n) because we are only traversing through the array once. The space complexity is O(n) because we dynamically allocated memory to the data structure which waas a hashset. T = using our first test case. we check if the array is empty, its not so we can proceed, we then check if the number is in seenNumbers, it isnt so we add the number to the seen numbers, then we go to the next element which is 2 and we check its not so add it again then we go to the next element which is 3 , and it is not so we add it again to the hash set, then we now stumble accross another 3 and we see that it is in the hash Set so we immeditaly call False."

        seenNumbers = set()

        for number in nums:
            if nums is None:
                return False
            if number not in seenNumbers:
                seenNumbers.add(number)
            else:
                if number in seenNumbers:
                    return True
        return False