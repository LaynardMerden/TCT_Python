n = int(input()) 
arr = list(map(int, input().split())) 
arr.sort()

cnt = 0 # 현재 그룹에 포함된 모험가의 수
res = 0 # 총 그룹의 수

for i in data:    # 공포도 낮은 순으로 하나씩
    cnt += 1      # i 공포도를 현재의 그룹에 넣어줌
    if cnt >= i:  # 현재 그룹에 포함된 모험가의 수가 공포도 i 보다 크거나 같으면 
        res += 1  # 그룹의 수를 늘려주고
        cnt = 0   # 현재 그룹에 포함된 모험가의 수를 0으로 초기화

print(res)
