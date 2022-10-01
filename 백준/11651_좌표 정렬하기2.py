# 백준 11651_좌표 정렬하기2


N = int(input())  # 점의 개수
lst = [list(map(int, input().split())) for _ in range(N)]  # 좌표
lst.sort(key=lambda x: (x[1], x[0]))  # y 기준 오름차순, 만약 y가 같으면 x 기존오름차순

for i in range(N):
    print("{} {}".format(lst[i][0], lst[i][1]))
