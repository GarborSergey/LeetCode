# Преобразование из римских чисел в арабские!
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000, }

        result = 0

        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX').replace('CD', 'CCCC').replace('CM', 'DCCCC')

        for i in range(len(s)):
            result += romans[s[i]]

        return result