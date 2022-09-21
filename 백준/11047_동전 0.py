# 백준 11047_동전 0


N, K = map(int, input().split())  # N: 동전 종류, K: 맞춰야 하는 금액
coin = [int(input()) for _ in range(N)]

remain = K  # 남은 금액
cnt = 0  # 동전 개수

for i in range(N-1, -1, -1):
    if coin[i] <= remain:
        cnt += remain//coin[i]
        remain -= coin[i] * (remain//coin[i])

print(cnt)
