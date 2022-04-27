# 1976. 시각 덧셈

t = int(input())
for tc in range(1, t+1):
    h1, m1, h2, m2 = map(int, input().split())
    if m1+m2 >= 60:
        m = m1 + m2 - 60
        h1 += 1
    else:
        m = m1 + m2
    if h1 + h2 > 12:
        h = h1 + h2 - 12
    else:
        h = h1 + h2
    print('#{} {} {}'.format(tc, h, m))