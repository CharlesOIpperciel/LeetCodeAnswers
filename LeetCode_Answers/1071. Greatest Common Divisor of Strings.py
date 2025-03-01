# Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str  # First input string
        :type str2: str  # Second input string
        :rtype: str      # The greatest common divisor (GCD) of the two strings
        """

        if str1 + str2 != str2 + str1:
            return ""  # No common divisor exists, return an empty string.

        min_length = min(len(str1), len(str2))

        # Iterate from the length of the shorter string down to 1. More efficient to go from the back because we will
        # find de largest common divisor without finding the small ones.
        for i in range(min_length, 0, -1):
            candidate = str1[:i]  # Take the first i characters of str1 as a potential common divisor.
            
            # Check if both strings can be formed by repeating this candidate.
            # This is done by checking if the lengths of str1 and str2 are divisible by i.
            if len(str1) % i == 0 and len(str2) % i == 0:
                # If str1  can be formed by repeating candidate len(str1) // i times.
                # If str2 can be formed by repeating candidate len(str2) // i times.
                if candidate * (len(str1) // i) == str1 and candidate * (len(str2) // i) == str2:
                    return candidate  # Return the candidate if both conditions are satisfied.
        
        return ""  # If no common divisor is found, return an empty string.

# Testing
print(Solution().gcdOfStrings("ABCABC", "ABC"))          # Output: "ABC"
print(Solution().gcdOfStrings("ABABABAB", "AB"))        # Output: "AB"
print(Solution().gcdOfStrings("LEET", "CODE"))          # Output: ""

# Time complexity: O(n)
# Space complexity: O(n) where n is the length of the shorter string. The function creates a candidate string that is a 
# substring of str1. The maximum size of this string is equal to the length of the shorter input string, min_length.

        