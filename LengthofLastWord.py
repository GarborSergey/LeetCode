# Получаешь строку из слов, вернуть длину последнего слова в строке
def lengthOfLastWord(s: str) -> int:
    lst = s.split()
    return len(lst[-1])