# 백준 1931_회의실 배정


N = int(input())  # 미팅 수
meeting = [list(map(int, input().split())) for _ in range(N)]  # 미팅 수요

meeting.sort(key=lambda x: (x[1], x[0]))  # 빨리 끝나는 순, 빨리 시작하는 순으로 정렬

cnt = 1  # 회의 개수
ed = meeting[0][1]  # 끝나는 시간

for i in range(1, N):
    if ed <= meeting[i][0]:
        cnt += 1
        ed = meeting[i][1]

print(cnt)
