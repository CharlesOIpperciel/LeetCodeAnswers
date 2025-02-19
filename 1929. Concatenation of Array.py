# Link:

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and 
# ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.Return the array ans.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

# Example 2:
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = nums 
        for i in range(len(nums)): # Iterate over the nums array and append each index starting from the start
            ans.append(nums[i])
        return ans
        

# Time complexity: O(n) because we traverse the array once all the way.
# Space complexity: I'm creating an extra n elements, so space complexity is O(n)


# In this version, i do what is ask and created a new array 'ans", instead of concatenating the nums array or playing
# with references of nums.

    def getConcatenation2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums  # Concatenating nums with itself

# Time complexity: O(n) because concatenation takes linear time.
# Space complexity: O(n) because a list of size 2n is created, so it's not in place.
    

print(Solution().getConcatenation([1,2,1]))
print(Solution().getConcatenation([1,3,2,1]))

print(Solution().getConcatenation2([1,2,1]))
print(Solution().getConcatenation2([1,3,2,1]))