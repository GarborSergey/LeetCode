# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.

class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) != 1:
            new = 0
            for n in num:
                new += int(n)
            num = str(new)

        return int(num)