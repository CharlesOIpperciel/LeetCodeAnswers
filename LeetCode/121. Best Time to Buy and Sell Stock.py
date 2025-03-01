# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your
# profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        lowest = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < lowest:
                lowest = price
            else:
                potential_profit = price - lowest
                if potential_profit > max_profit:
                    max_profit = potential_profit

        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
print(Solution().maxProfit([1, 2, 3, 4, 5]))  # 4

# Time complexity: O(n), n being the length of prices. We iterate through prices once to find the maximum profit.

# Explanation: We initialize the lowest price to the first price in the list. We initialize the maximum profit to 0.
# We then iterate through the list starting from the second element. If the current price is lower than the lowest
# price, we update the lowest price to the current price. If the current price is not lower than the lowest price,
# we calculate the potential profit by subtracting the lowest price from the current price. If the potential profit
# is greater than the maximum profit, we update the maximum profit to the potential profit. We continue this process
# until we reach the end of the list. We then return the maximum profit.
