class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        if len(s) != len(t):
            return False
        
        for letter in s:
            if letter in count_s:
                count_s[letter] += 1
            else:
                count_s[letter] = 1
        for letter in t:
            if letter in count_t:
                count_t[letter] += 1
            else:
                count_t[letter] = 1

        if count_s == count_t:
            return True
        else:
            return False
