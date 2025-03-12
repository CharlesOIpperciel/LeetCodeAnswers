# Link: https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the 
# array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.


# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0  # Tracks the farthest reachable index
        
        for i in range(len(nums)):
            if i > farthest:  # If we are stuck at a point we can't jump from
                return False
            
            farthest = max(farthest, i + nums[i])  # Update the farthest index reachable
            
            if farthest >= len(nums) - 1:  # If we can reach or go beyond the last index
                return True
        
        return False  # If we exit the loop without reaching the last index


print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))