s = input()
result = int(s[0])

for i in s[1:]:
    if result == 0:
        result += int(i)
    elif int(i) != 0:
        result *= int(i)

print(result)
