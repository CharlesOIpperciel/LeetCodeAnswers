# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of 
# candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, 
# they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.

 

# Example 1:
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

# Example 2:
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false] 
# Explanation: There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

# Example 3:
# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]
 

# Constraints:
# n == candies.length
# 2 <= n <= 100
# 1 <= candies[i] <= 100
# 1 <= extraCandies <= 50

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        most_candies = []
        curr_max = max(candies)
        for i in range(len(candies)):
            if (curr_max - candies[i]) <= extraCandies:
                most_candies.append(True)
            else:
                most_candies.append(False)
        
        return most_candies


print(Solution().kidsWithCandies([2,3,5,1,3], 3))
print(Solution().kidsWithCandies([4,2,1,1,2], 1))
print(Solution().kidsWithCandies([12,1,12], 10))

# Analysis

# Time complexity: I use max(candies) so O(n) there. we iterate len(candies) times at worst, so O(n). Total = O(n) + O(n) so O(n) 
# Space complexity: we used a new array most_candies and populated with inputs the size of the candies input array. So O(n).
# curr_max stores an integer, so constant space O(1). Overall, still O(n)

# 2nd cleaner implementation with 1 liner:
class Solution2(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        curr_max = max(candies)
        return [(candy + extraCandies) >= curr_max for candy in candies]


print(Solution2().kidsWithCandies([2,3,5,1,3], 3))
print(Solution2().kidsWithCandies([4,2,1,1,2], 1))
print(Solution2().kidsWithCandies([12,1,12], 10))

# Same analysis.