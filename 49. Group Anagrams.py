# Link: https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            hashmap[sorted_s].append(s)

        return hashmap.values()


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Analysis:
# 1. Initialize a `defaultdict()` called `hashmap`,
# 2. It iterates through each string `s` in the input list.
# 3. For each string `s`, it sorts the characters to get the sorted version `sorted_s`.
# 4. It checks if `sorted_s` is not in the `hashmap`. If not, it initializes an empty list for that key in `hashmap`.
# 5. It then appends the original string `s` to the list associated with the key `sorted_s` in `hashmap`.

# Complexity:
# We have to, at worst iterate through each s in strs, so we have a O(n) time complexity
# n is the number of strings in `strs` stored in the `hashmap`, and m is the average length of each string. so we have
# a space complexity of, at worst, O(n*m)
