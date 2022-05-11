# Дана строка, найти длину самой длинной подстроки с неповторяющимися символами
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substring = ''  # the substring being checked
        longest = 0  # length of the longest substring
        for char in s:
            substring += char  # append char in substring
            if substring.count(char) > 1:  # check repeat
                # if char is repeating,
                # substring = substring starts with an index without the FIRST encountered repeated character
                # example:
                # s = 'asjrgapa'
                # when substring = 'asjrga' ---> substring = 'sjrga' on the next substring = 'sjrgap' ...
                substring = substring[substring.index(char) + 1:]
            longest = len(substring) if longest < len(substring) else longest  # check len is longest

        return longest