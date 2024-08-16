# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
# the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence o
# f "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

class Solution(object):

    def isSubsequence(self, s, t):
        
        letter_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        # If s it empty, then it's a subsequence of t
        if (len(s) == 0):
            return True
        
        # If s contains something other than an english lowercase letter, return False
        for letter in s:
            if letter not in letter_array:
                return False
        
        # If t contains something other than an english lowercase letter, return False
        for letter in t:
            if letter not in letter_array:
                return False
            
        # Actual logic. If a letter from s is not in t, then it's not a subsequence
        for letter in s:
            if letter not in t:
                return False
            else:
                t = t[t.index(letter)+1:]
            
        return True
    
print(Solution().isSubsequence('abc', 'ahbgdc'))  # True
print(Solution().isSubsequence('axc', 'ahbgdc'))  # False
print(Solution().isSubsequence('acb', 'ahbgdc'))  # False

# Time complexity: O(n), n being the length of s. We iterate through s once to check if it's a subsequence of t.

# Explanation:
# We first check if s is empty. If it is, then it's a subsequence of t. We then check if s contains any letter that is
# not an english lowercase letter. If it does, we return False. We do the same for t. If t contains any letter that is not
# an english lowercase letter, we return False. We then iterate through s. If a letter from s is not in t, we return False.
# If it is in t, we update t to be the rest of the string after the index of the letter. If we get through the entire loop,
# then s is a subsequence of t, and we return True.