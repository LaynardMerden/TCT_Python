# n 입력 받음
n = int(input()) 
# n명의 모험가의 공포도 입력 받아서 arr에 list로 저장
arr = list(map(int, input().split())) 

cnt = 0 # idx 역할 (현재 그룹에 포함된 모험가의 수 저장)
res = 0 # 현재 만들어진 그룹의 수
arr.sort() # list를 오름차순으로 정렬. (공포도 낮은 모험가부터 하나씩 grouping)

# 오름차순으로 정렬된 arr에 대해 공포도가 i인 경우 i 명씩 grouping 해 나가면서
# cnt 와 res update (cnt < n)
while cnt < n:
    if arr[cnt] + cnt <= n:
        cnt += arr[cnt]
        res += 1
    else:
        break

print(res)
