# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

# First iteration of my solution, not efficient, but works. O(n^2)
class Solution(object):

    def isVowel(self, letter):
        accepted_vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        if letter in accepted_vowels:
            return True
        else:
            return False
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Initialise an empty array to return the final word
        final_word = ""
        
        # Iterate through s in reverse to get all vowels, in reverse order. Then create a new array with that.
        vowel_array = []
        for letter in s[::-1]:
            if self.isVowel(letter):
                vowel_array.append(letter)
                
        # Iterate over every letter of s, then swap the vowels:    
        for i in range(len(s)):
            if self.isVowel(s[i]):
                final_word += vowel_array[0]
                vowel_array.pop(0) # Remove the vowel from index 0 from vowel_array since you swapped it with the vowel from original word s
            else:
                final_word += s[i]
                
        return final_word
                
        

print(Solution().reverseVowels("IceCreAm"))
print(Solution().reverseVowels("leetcode"))

# Analysis

# Time complexity: we iterate over s to get vowel_array so O(n). We iterate of range(len(s)), so O(n), but then pop() shifts all elements 
# of vowel_array to the left, so O(n) again. Total: O(n) + O(n^2)
# Space complexity: Final_string and vowel array was created. so O(n) for both. Total O(n)

class Solution2(object):
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s = list(s)  # Convert string to list for mutability
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)

print(Solution2().reverseVowels("IceCreAm"))
print(Solution2().reverseVowels("leetcode"))

# Analysis:

# Time: O(n)
# Space: O(1)
        