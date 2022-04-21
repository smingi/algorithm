# 백준 11052 카드 구매하기


N = int(input())
cards = list(map(int, input().split()))

D = [0] * N  # DP 사용
D[0] = cards[0]
for i in range(1, N):
    for j in range(i):
        if D[i] < max(D[j]+D[i-j-1], cards[i]):
            D[i] = max(D[j]+D[i-j-1], cards[i])
print(D[N-1])
