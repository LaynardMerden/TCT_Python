# 상하좌우

n = int(input())
mov = list(input().split())

x, y = 1, 1

for i in mov:
    if (i == 'R'):
        if y < n: y += 1
    elif (i == 'U'):
        if x > 1: x -= 1
    elif (i == 'D'):
        if x < n: x += 1
    elif (i == 'L'):
        if y > 1: y -= 1

print (x, y)
