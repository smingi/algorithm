# 백준 21758 꿀 따기


def move(b2):  # 벌 -> 벌 -> 벌통
    global sumv
    bee1 = honeys[-1] - lst[0] - lst[b2]
    bee2 = honeys[-1] - honeys[b2]
    sumv = max(sumv, bee1 + bee2)


def move2(b2):  # 벌통 <- 벌 <- 벌
    global sumv
    bee1 = honeys[-1] - lst[-1] - lst[b2]
    bee2 = honeys[b2] - lst[b2]
    sumv = max(sumv, bee1 + bee2)


def move3(honey):  # 벌 -> 벌통 <- 벌
    global sumv
    bee1 = honeys[honey] - lst[0]
    bee2 = honeys[-1] - honeys[honey-1] - lst[-1]
    sumv = max(sumv, bee1 + bee2)


N = int(input())  # 장소 개수
lst = list(map(int, input().split()))  # 꿀 정보 리스트
honeys = [lst[0]]  # 꿀의 누적합
sumv = 0  # 최대합(결과)

for i in range(1, N):  # 꿀의 누적합 구하기
    honeys.append(honeys[i-1] + lst[i])

for b in range(N):
    if 0 < b < N:  # 2번째 벌 위치
        move(b)
    if 0 <= b < N-1:  # 2번째 벌 위치
        move2(b)
    if 0 < b < N-1:  # 벌통 위치
        move3(b)

print(sumv)
