# Link: https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most
# frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

from collections import defaultdict


class Solution(object):

    # Variant 1:
    # Initialize a defaultdict(). Then we iterate through that dictionary and add each to each key (distinct elements
    # in nums) the amount of occurrences. Then we have to sort that dictionary using the 3 parameters in the sorted().
    # We need to make sure that we sort it from the highest value to the lowest (We want the top K elements). We can
    # then check for each item in that sorted dictionary from the index 0 to k, and return the first k keys

    # Time complexity analysis: we have to check for all the num in nums so O(n). We then have to sort the array and
    # it's usually O(nlogn) in average cases, depending on the amout of items being sorted. We then have to iterate to
    # k, so O(k). Conclusion: the dominant factor is O(nlogn) so our solution is O(nlogn)
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashmap = defaultdict()

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        top_k_elements = []
        for item in sorted_hashmap[:k]:
            top_k_elements.append(item[0])

        return top_k_elements

    # Variant 2: with a time complexity of O(n):
    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        # This array only needs to be as big as the array nums
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            # Count the number of occurrences of each value in nums, put it in a hashmap value : occurrences
            count[num] = 1 + count.get(num, 0)
        for num, c in count.items():
            # For every num in our hashmap, we map that num to its respective index 'c' that represents the number
            # occurrences
            freq[c].append(num)

        # We start building our result
        result = []
        # We iterate from the back of freq, because we want the values that occurred the most
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                # We can stop when result == k, because we don't need more
                if len(result) == k:
                    return result


print('\nVariant 1')
print(Solution().topKFrequent([-1, -1], 1))
print(Solution().topKFrequent([5, 4, 5, 1, 1, 1, 2, 3, 2, 1, 5], 2))
print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))

print('\nVariant 2')
print(Solution().topKFrequent2([-1, -1], 1))
print(Solution().topKFrequent2([5, 4, 5, 1, 1, 1, 2, 3, 2, 1, 5], 2))
print(Solution().topKFrequent2([1, 1, 1, 2, 2, 3], 2))
