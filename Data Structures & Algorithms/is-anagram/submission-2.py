class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        map1 = {}
        map2 = {}
            
        for char in s:
            if char not in map1:
                map1[char] = 1
            else:
                map1[char] += 1

        for char in t:
            if char not in map2:
                map2[char] = 1
            else:
                map2[char] += 1

        if map1 != map2:
            return False
            
        return True  
            
            
             # "R: This problem is basically asking us to check whether the two inputs are anagrams. Two strings are anagrams if they contain the same characters with each other character appearing the same number of times, regardless of the order."
       #  " E: 1) If the one string empty and the other isnt then return false II) If There is nothing in both strings then return True.
       # A: Ok so my brute force approach would first of all check the lengths of the two strings, then i would have two pointers one for each string. so i in the first string would check if its equal to j of the first letter in the second string, then i would also have a counter variable for each letter which would be updated each time we find a match. then we would check the counter for both strings and see if they are equal, if they are then we would return true, if they arent then return false. The time complexity for this would be o(n^2) because of the nested loops and the space complexity would be O(n) because we have created a counter variable so we have created extra space. My Optimal approach would be to introduce a hashmap that would keep a frequency count for each letter in both strings. so then we can now compare if the two hashmaps are equal or not. but we alsop have to make sure that the lenght of s is = to the lenght of t first. so everything being equal then yes, return true, else return false. The trime complexity for thius would be O(n) because we intorduces 2 hashmaps and when u add them togethjer u drop the constant which gives us O(n) and the space complexity would be  O(n) too becuase of the extra storage.
       # "C: "
       # "T: "