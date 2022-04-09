# 6019. 기차 사이의 파리

t = int(input())
for tc in range(1, t+1):
    d, a, b, f = map(int, input().split())
    distance = 0
    while d >= 0.000001:
        t = d / (f+b)  # 시간 = 거리 / 속도
        distance += d - b * t  # 거리 = 시간 * 속도
        d = f * t - a * t
        if d <= 0:
            break
        t = d / (f+a)
        distance += d - a * t
        d = f * t - b * t
    print('#{} {}'.format(tc, distance))