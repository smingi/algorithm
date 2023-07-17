# 백준 16953_A -> B


from collections import deque


def A_to_B():  # A -> B
    q = deque()
    q.append(A)
    dic[A] = 1

    while q:
        now = q.popleft()

        if now == B:  # 찾은 경우
            print(dic[B])
            return

        for new in [now * 2, now * 10 + 1]:  # 갈 수 있는 방법
            if 0 < new <= B and new not in dic:  # 범위내 방문하지 않은 곳
                q.append(new)
                dic[new] = dic[now]+1

    print(-1)  # 찾지 못한 경우


A, B = map(int, input().split())  # A: 시작 숫자, B: 목표 숫자
dic = dict()  # 방문여부 체크
A_to_B()  # A -> B
