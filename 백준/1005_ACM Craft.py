# 백준 1005_ACM Craft

import sys
from collections import deque


def get_time():  # W 건물을 짓는데 걸리는 시간 구하기
    dp = [0] * (N+1)
    q = deque()

    for i in range(1, N+1):  # 건설할 수 있는 건물 짓기
        if pre_cnt[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        now = q.popleft()  # 현재 건설하는 건물

        for new in new_work[now]:
            pre_cnt[new] -= 1
            dp[new] = max(dp[new], dp[now] + time[new])

            if pre_cnt[new] == 0:  # 미리 지어야할 건물을 다 지은 경우
                q.append(new)

        if pre_cnt[W] == 0:  # W 건물이 완성된 경우 출력하고 종료
            print(dp[W])
            break


T = int(input())  # 테스트케이스
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())  # N: 건물의 수, K: 건물순서 규칙의 총 개수
    time = [0] + list(map(int, sys.stdin.readline().split()))  # 각 건물당 걸리는 시간(인덱스를 맞춰주기 위해 앞에 0을 추가)
    new_work = [[] for _ in range(N + 1)]  # 건설하면 새롭게 건설할 수 있는 건물 목록
    pre_cnt = [0] * (N+1)  # 먼저 지어야 하는 건물의 남은 개수

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())  # X -> Y 건물짓는 순서
        new_work[X].append(Y)
        pre_cnt[Y] += 1

    W = int(sys.stdin.readline().strip())  # 승리하기 위해 건설해야 할 건물의 번호

    get_time()  # W 건물을 짓는데 걸리는 시간 출력
