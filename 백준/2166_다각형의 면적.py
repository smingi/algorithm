# 백준 2166_다각형의 면적


N = int(input())  # N각형
location = [list(map(int, input().split())) for _ in range(N)]  # 좌표
location += [location[0]]
x = 0
y = 0

for i in range(N):
    x += location[i][0] * location[i+1][1]
    y += location[i][1] * location[i+1][0]

print(abs(round((x - y)/2, 1)))
