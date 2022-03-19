# 3431. 준환이의 운동관리

t = int(input())
for tc in range(1, t+1):
    low, high, now = map(int, input().split())
    result = 0  # 결과
    if now > high:
        result = -1
    else:
        temp = low - now
        if temp >= 0:
            result = temp
        else:
            result = 0
    print('#{} {}'.format(tc, result))