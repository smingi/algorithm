# 백준 11650 좌표 정렬하기


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()

for i in range(len(lst)):
    print("{} {}".format(lst[i][0], lst[i][1]))
