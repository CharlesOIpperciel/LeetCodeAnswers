# Link: https://leetcode.com/problems/valid-anagram/description/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

class Solution(object):

    # Variant 1: uses a hashmap. Time complexity of O(n), n being the len(s).
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        # Dictionaries to count the occurrences of each letters
        count_s = {}
        count_t = {}

        # This line increments the count of the character s[i] in the count_s dictionary. If the character doesn't
        # exist in the dictionary, it initializes its count to 1 using the get() method. Same goes for count_t
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t

    # Variant 2: straight comparison. Fewer lines. we join the empty string, with every element of the string in order.
    # if it's an anagram, it should technically be the same.
    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return ''.join(sorted(s)) == ''.join(sorted(t))


print('Variant 1: use of hashmap')
print(Solution().isAnagram('anagram', 'nagaram'))
print('\n')
print('Variant 2: straight comparison with the use of .join and sorted()')
print(Solution().isAnagram2('anagram', 'nagaram'))
