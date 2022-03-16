# 2806. N-Queen


def is_safe(k, i):  # 퀸을 놓아도 되는지 확인하는 함수
    for m in range(N):
        if visited[k][m] == 1:  # 좌우 확인
            return
        if visited[m][i] == 1:  # 상하 확인
            return
        if 0 <= k+m < N and 0 <= i+m < N:  # 오른쪽 위 대각선 확인
            if visited[k+m][i+m] == 1:
                return
        if 0 <= k-m < N and 0 <= i+m < N:  # 오른쪽 아래 대각선 확인
            if visited[k-m][i+m] == 1:
                return
        if 0 <= k+m < N and 0 <= i-m < N:  # 왼쪽 위 대각선 확인
            if visited[k+m][i-m] == 1:
                return
        if 0 <= k-m < N and 0 <= i-m < N:  # 왼쪽 아래 대각선 확인
            if visited[k-m][i-m] == 1:
                return
    return True  # 문제가 없으면 안전


def Qlocation(k):  # 퀸을 놓을 위치를 찾는 함수
    global cnt
    if k == N:  # 마지막 칸까지 다 놓았으면 정지
        cnt += 1
        return

    for i in range(N):  # 퀸을 놓을 수 있는 자리 탐색
        if not visited[k][i]:
            if is_safe(k, i):  # 퀸을 놓아도 되는지 확인
                visited[k][i] = 1  # 방문 표시
                Qlocation(k+1)  # 다음 칸으로 이동
                visited[k][i] = 0  # 방문 표시 원상복귀


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]  # 방문여부 확인 리스트
    cnt = 0  # 놓을 수 있는 방법 개수
    Qlocation(0)  # 퀸 위치를 찾는 함수

    print('#{} {}'.format(tc, cnt))
