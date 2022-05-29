# Given a string array words,
# return the maximum value of length(word[i]) * length(word[j]
# ) where the two words do not share common letters. If no such two words exist, return 0.

# Подсмотрел про использование множеств и про то что циклами нужно идти после слов, которые уже проверенны

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        result = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(set(words[i]).intersection(words[j])) == 0:
                    result = max(result, len(words[i]) * len(words[j]))

        return result