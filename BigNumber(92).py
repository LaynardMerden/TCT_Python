# 큰 수의 법칙

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

arr.sort(reverse=True) # 입력된 수들 내림차순으로 정렬

while m > 0:
    if m > k: # 남은 더해야 할 수(m)가 k보다 큰 경우
        m -= k+1
        res += arr[0]*k + arr[1] #가장 큰 수를 k번 더하고 두번째로 큰 수를 한번 더한다.
    else: # 남은 더해야 할 수(m)가 k보다 작거나 같은 경우
        m = 0
        res += arr[0]*m #가장 큰 수를 m번 더한다.

print(res)
