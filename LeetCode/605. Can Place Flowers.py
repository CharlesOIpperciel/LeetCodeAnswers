# Link: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted 
# in adjacent plots.Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
# and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers 
# rule and false otherwise.

 

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 
# Constraints:
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0  # Count of flowers we can plant
        
        for i in range(len(flowerbed)):
            # Check if the current spot is empty and the adjacent spots are also empty. More Precisely, it checks three things:
            
            # 1 - The current position must be empty (flowerbed[i] = 0).
            # 2 - If it's the first poisition, but there's no left neighbor OR If it's not, the left neighbor must be empty
            # 3 - If it's the last position, there's no right neighbor OR if it's not, the right neighbor must be empty
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1  # Plant a flower
                count += 1  # Increment the count of planted flowers
            
            if count >= n:  # If we have planted enough flowers, return True
                return True
        
        return count >= n  # Return if we have planted at least n flowers

# Test cases
print(Solution().canPlaceFlowers([1,0,0,0,1], 1))  # Output: true
print(Solution().canPlaceFlowers([1,0,0,0,1], 2))  # Output: false

# Analysis

# Time: we ieterate len(flowerbed) times in the worst scenario, so O(n)
# Space: We created a new variable called count, so O(1)
