# Link: https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

# Iteration 1 of the solution (Naive way)
class Solution(object):

    def longest(self,a,b):
        if len(a) > len(b):
            return a
        return b

    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        final_string = []
        longer_string = self.longest(word1,word2)

        for index in range(len(longer_string)):
            if index < len(word1):
                final_string.append(word1[index])
            if index < len(word2):
                final_string.append(word2[index])
        return "".join(final_string)
        

# Test the solution
print(Solution().mergeAlternately("abc","pqr"))
print(Solution().mergeAlternately("abc","pqras"))
print(Solution().mergeAlternately("abcas","pqr"))
print(Solution().mergeAlternately("abcsdfdsfd","p"))

# This solution is the very first iteration of it, it is by far not optimal

# Time and space complexity analysis
# Time: we iterate, in the worst scenario possible, n times, n being the length of the longest string. After that, we iterate one last n times thru the whole final string
# to turn the [] into a concatenated string. So O(2n). Since the constant 2 is meaningless in the Big O notation. the final answer is O(n)
# Space: The space complexity is O(n + m), where n is the length of word1 and m is the length of word2. This is due to the creation of the final_string list that holds all characters 
# from both input strings before converting it to a final string.


# Iteration 2 of the solution (same efficiency, but little different as I append a subset of word1 and word2)
class Solution2(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        final_string = []
        i = 0
        j = 0

        while i < len(word1) & j < len(word2):
            final_string.append(word1[i])
            final_string.append(word2[j])
            i += 1
            j += 1

        if i < len(word1):
            final_string += word1[i:]

        if j < len (word2):
            final_string += word2[j:]


        return "".join(final_string)
    
print(Solution2().mergeAlternately("abc","pqr"))
print(Solution2().mergeAlternately("abc","pqras"))
print(Solution2().mergeAlternately("abcas","pqr"))
print(Solution2().mergeAlternately("abcsdfdsfd","p"))

# Time and space complexity analysis
# Time: Same thing here, we also iterate in the worst scenario possible, as much as the longest length of the two words. Then re-iterate n times again at the end to concatenate. So, O(2n) = O(n)
# Space: Same as previous.