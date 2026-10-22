class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # R: The question is asking us to return truew if s reads the same backwards, false if it doesnt. Eg. noon. it is also read as noon backwards too.
        # E: First edge case is if the string is empty, return True. 
        # A: My approach to this problem would be to have two pointers. One pointing to the the start and the other pointing at the end, and what i would do is work my way forward by increasing the i pointer and decreasing the j pointer until they meet in the middle. once they meet in the middle and eveyrthing is equal then ill return true, else ill return false if theres ever a mismatch. the time complexity for this problem would be o(n) because we are iterating throggh the list once and only moving the pointers. Space complexity is O(1) because there is no auxilary space. Also just to note, if there appears punctuations, spaces etc we ignore it too.
        # C:
        # T:


        left = 0
        right = len(s) - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1 
                continue

            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
               
        return True