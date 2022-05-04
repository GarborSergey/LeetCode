# Implement strStr().
#
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf()

def strStr(self, haystack: str, needle: str) -> int:
    if needle in haystack:
        plus = 0
        while True:  # go through all
            # Whether the found character is our substring?
            if haystack[haystack.index(needle[0]): haystack.index(needle[0]) + len(needle)] == needle:
                return haystack.index(needle[0]) + plus  # return id with plus
            else:
                # You need to remove the character that did not pass the 'if'
                plus += 1  # if a character is removed all the following indices decrease by 1
                haystack = haystack.replace(needle[0], '', 1)  # remove char
    else:
        return -1
