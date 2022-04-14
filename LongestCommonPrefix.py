# Найти самую длинную начальную подстроку общую для каждой строчки
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        substring = strs[0]
        del strs[0]
        counter = 0
        while counter < 199:
            counter += 1
            if substring == '':
                break

            for string in strs:
                if substring == string[:len(substring)]:
                    continue
                else:
                    substring = substring[:-1]

        return substring
