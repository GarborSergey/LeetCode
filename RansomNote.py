# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine = list(magazine)
        counter = 0
        for char in ransomNote:
            for char_m in magazine:
                if char == char_m:
                    counter += 1
                    magazine.remove(char_m)
                    break

        result = counter >= len(ransomNote)
        return result