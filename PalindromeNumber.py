# Является ли данное чило палиндромом
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False

x = '12324'
print(reversed(x))