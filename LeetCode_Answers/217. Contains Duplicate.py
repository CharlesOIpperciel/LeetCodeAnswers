# Link: https://leetcode.com/problems/contains-duplicate/
import self


# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
# element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution(object):

    # Variant 1: brute force with O(n^2) time complexity because we have two loops. This method works, but isn't good
    # and exceeds the time limit, so we have to come up with a better solution.
    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    # Variant 2: uses a hashmap to get the elements in O(1), but still have a time complexity of O(n) because we use a
    # loop and iterate at worst, n times.
    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


print('Variant 1: works but exceeds time limit because its in O(n^2)')
print(Solution().containsDuplicate1([1, 2, 3, 1]))
print('\n')
print('Variant 2: works in O(n) and uses a hashmap to get the elements in O(1)')
print(Solution().containsDuplicate2([1, 2, 3, 1]))
