# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
num = [1,2,0,0]
k = 34
numbers_list = ''.join([str(n) for n in num])
result = int(numbers_list) + k
z = list(str(result))
print([int(n) for n in z])
