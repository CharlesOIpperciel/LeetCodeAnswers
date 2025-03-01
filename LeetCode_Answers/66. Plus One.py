# Link: https://leetcode.com/problems/plus-one/description/
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the 
# integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer 
# does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        for i in range(n - 1, -1, -1): # Iterate through the whole thing from the end
            if digits[i] < 9:
                digits[i] += 1 # we increment and return digits
                return digits
            digits[i] = 0 # we put it to 0 and then go to the next iteration
        return [1] + digits # add a 1 at the first index

# Testing
print(Solution().plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(Solution().plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(Solution().plusOne([9]))  # Output: [1, 0]
print(Solution().plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]

# Time and space complexity analysis:
# Time complexity is, in the worst case, O(n) be cause we traverse all the elements in digits, so n, to end up with a
# 1 a the first index.

# Space complexity O(1) because we modify the list digits in place, meaning no extra memory is used. However, in the
# worst case, when all digits are 9s, I create a new list with an extra digit [1,0,0,0]. So the Space complexity is O(n)
# in that case.
