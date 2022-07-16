# 백준 1654_랜선 자르기


K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

st = 1
ed = max(lines)

while st <= ed:
    mid = (st+ed)//2
    cnt = 0

    for line in lines:
        cnt += line//mid

    if cnt >= N:
        st = mid + 1
    else:
        ed = mid - 1

print(ed)
