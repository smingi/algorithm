# 4299. 태혁이의 사랑은 타이밍

t = int(input())
for tc in range(1, t+1):
    d, h, m = map(int, input().split())

    d -= 11
    h += d*24
    if h - 11 >= 0:
        h -= 11
        m += h*60-11
        if m >= 0:
            result = m
        else:
            result = -1
    else:
        result = -1

    print('#{} {}'.format(tc, result))