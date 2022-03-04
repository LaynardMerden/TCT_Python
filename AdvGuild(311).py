n = int(input())
arr = list(map(int, input().split()))

cnt = 0
res = 0
arr.sort(reverse=True)

while cnt < n:
    if arr[cnt] + cnt <= n:
        cnt += arr[cnt]
        res += 1
    else:
        break

print(res)
