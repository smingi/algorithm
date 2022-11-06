# 백준 12852_1로 만들기 2


from collections import deque


def make_One():
    q = deque()
    q.append([N, [N]])  # 현재위치, 지나온 경로

    while q:
        now, sequence = q.popleft()  # 현재위치, 지나온 경로

        if now == 1:  # 도착지
            print(len(sequence) - 1)  # 이동 횟수
            print(" ".join(map(str, sequence)))  # 이동 경로
            return

        if now % 3 == 0:  # 이동방법 1
            new = now // 3

            if new not in dp:
                dp[new] = 1
                q.append([new, sequence + [new]])

        if now % 2 == 0:  # 이동방법 2
            new = now // 2

            if new not in dp:
                dp[new] = 1
                q.append([new, sequence + [new]])

        if now > 1:  # 이동방법 3
            new = now - 1

            if new not in dp:
                dp[new] = 1
                q.append([new, sequence + [new]])


N = int(input())  # 1로 만들 숫자
dp = dict()
make_One()  # 1로 만들기
