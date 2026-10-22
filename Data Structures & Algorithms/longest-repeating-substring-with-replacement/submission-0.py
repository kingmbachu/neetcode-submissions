class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = {}
        longest = 0

        for right in range(len(s)):
            char = s[right]  
        
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    # replacementNeeded = Window size - MaxFreq
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest