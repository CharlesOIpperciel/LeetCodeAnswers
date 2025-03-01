# Link: https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
# to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    # Variant 1: Brute force, so time complexity of O(n^2). Naive way of doing this problem.
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Iterate through the beginning to the end - 1, because the last element doesn't have anything after to compare.
        # Then we iterate again inside the first loop, but from the element after the i. We look if they add up to the
        # target. If so, then we found the two indexes we need.
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

    # Variant 2: Here, we use a hashmap. we create an enumerate(), then we calculate the difference. If we take a closer
    # look at the problem. For every element at a specific iteration, we only need to find the difference between target
    # and the element itself. So that's we do here. We look at each iteration, if the 'difference' is in the hashmap, if
    # yes, then that means we found our two elements that adds up to the target. hashMap[difference] return the value at
    # the key difference, which is in our case, the index. if difference in hashMap returns False, we add the index.
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}  # value : index

        for index, num in enumerate(nums):
            difference = target - num
            if difference in hashMap:
                return hashMap[difference], index
            hashMap[num] = index


print('Variant 1: Naive way of doing it. Brute force with time complexity of O(n^2)')
print(Solution().twoSum1([2, 7, 11, 15], 9))
print('\n')
print('Variant 2: Use of a hashmap. Time complexity of O(n), but we use some space here.')
print(Solution().twoSum2([2, 7, 11, 15], 9))
