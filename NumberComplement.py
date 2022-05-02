# The complement of an integer is the integer you get when you flip all
# the 0's to 1's and all the 1's to 0's in its binary representation.
#
#     For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
#
# Given an integer num, return its complement.

class Solution:
    def findComplement(self, num: int) -> int:
        b = ''
        while num > 0:
            b = str(num % 2) + b
            num = num // 2

        bin_num = ''
        for i in b:
            if i == '0':
                bin_num += '1'
            else:
                bin_num += '0'

        return int(bin_num, 2)