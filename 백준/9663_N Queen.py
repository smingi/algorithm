# 백준 9663_N Queen (pypy 사용)


def check(idx):
    for i in range(idx):
        if row[idx] == row[i] or abs(row[idx] - row[i]) == idx - i:
            return False

    return True


def dfs(k):
    global cnt

    if k == N:  # N개의 퀸을 놓으면 종료
        cnt += 1
        return

    for i in range(N):
        row[k] = i
        if check(k):  # 조건에 맞으면 다움칸으로
            dfs(k+1)


N = int(input())  # N: 퀸의 개수
row = [0] * N  # 행에 놓인 퀸의 열 위치

cnt = 0  # 놓는 방법 개수
dfs(0)  # 깊이 우선 탐색

print(cnt)
