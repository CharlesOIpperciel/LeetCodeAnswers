# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day. On each day, you may 
# decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy 
# it then immediately sell it on the same day. Find and return the maximum profit you can achieve.


# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

# Constraints:
# 1 <= prices.length <= 3 * 104 
# 0 <= prices[i] <= 104

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        current_price = 0 # Pointer 1 
        last_price = 0 # Pointer 2
        
        for i in range(len(prices)):
            if i == 0:
                last_price = prices[i] # First price of the prices array
            else:
                current_price = prices[i] # the current price we're on right now
                if current_price <= last_price: # if its higher than last price, than we make no profit
                    last_price = current_price
                    continue
                elif current_price > last_price: # if its lower than last price, than we make profit
                    profit += (current_price - last_price) # Increment profit by the profit we just made
                    last_price = current_price # point to the next price
                    
        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))


# Analysis

# Time: O(n) because we iterate len(prices) times.
# Space: O(1) because we created three new variables, only O(1) for each.
            
