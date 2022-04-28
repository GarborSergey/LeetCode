abc = 'ABCD....'
n = 10  # Input info
result = ''
while n > 0:
    n = n - 1
    result += abc[n % 26]
    n //= 26

print(result)