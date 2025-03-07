# Link: https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]

# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# first solution, it works but its not what is asked. I need to modify nums in-place. its also not efficient at all as insert() and pop()
# makes it O(n^2)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        final_array = []
        
        for i in range(len(nums)-1,-1,-1):
            if k == 0:
                final_array.extend(nums)
                return final_array
            else:
                final_array.insert(0, nums[i])
                nums.pop()
                k -= 1
        
        return final_array

# print(Solution().rotate([1,2,3,4,5,6,7], 3))
# print(Solution().rotate([-1,-100,3,99], 2))

# Optimal solution 
class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k %= len(nums) # if k > len(nums) we only want that
        
        # reverse the whole array
        nums.reverse()
        
        # reverse the first k elements
        nums[:k] = reversed(nums[:k])
        
        # Reverse the rest of the elements
        nums[k:] = reversed(nums[k:])
        
        return nums

print(Solution2().rotate([1,2,3,4,5,6,7], 3))
print(Solution2().rotate([-1,-100,3,99], 2))

# Analysis
# Time: O(n) * 3 for each reverse operation, so total = O(n)
# Space: O(1) because everything is done in place, no new memory was needed as we deal with nums directly.
# See annexe at the end of my notebook.
