# Дана строка, найти длину самой длинной подстроки с неповторяющимися символами
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

s = 'wqdasasdads'
set_s = set(s)
list_s = list(s)
ans = []
for i in range(len(list_s)):
    if i == len(list_s)-1:
        break
    if list_s[i] != list_s[i+1]:
        ans.append(i)
print(ans)
