# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s += ' '

        def convertor(s: str) -> str:
            repeat = dict()
            counter = 0
            result = []

            if ' ' in s:
                transit = s.split()
            else:
                transit = list(s)

            for char in transit:
                if char not in repeat.keys():
                    repeat[char] = counter
                    counter += 1

                result.append(repeat[char])

            return result

        return convertor(s) == convertor(pattern)
