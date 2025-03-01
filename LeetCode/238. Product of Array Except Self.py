# https://leetcode.com/problems/product-of-array-except-self/


# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space
# for space complexity analysis.)

from collections import defaultdict


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # We initialize a result array. Then we compute the prefixes first. It starts with 1 because there's nothing to
        # the left of the result array. Then we iterate through the array from the beginning to the end. We then set the
        # result at that position i to the prefix, then we multiply the prefix by the value in nums. We do the same
        # logic with the postfix, but we iterate from the back. We then return Result

        # Time complexity analysis: it's in O(n) because we iterate through the array once. then we iterate again. So
        # O(n) + O(n) gives us a time complexity of O(n)
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result


print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
