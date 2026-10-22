class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # STEP 1: Initialise variables
        left = 0
        right = 0
        count = {}
        longest = 0

        #Step 2: Expand the Window
        for right in range(len(s)):
            char = s[right]  
        
            #Step 3: Update the frequency count
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    #Step 4: Shrink invalid window
    # replacementNeeded = Window size - MaxFreq
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            # Step 5: Update longest valid window
            longest = max(longest, right - left + 1)
        return longest