# 백준 10814_나이순 정렬


N = int(input())
lst = [list(input().split()) for _ in range(N)]

lst.sort(key=lambda x: int(x[0]))

for i in range(len(lst)):
    print("{} {}".format(lst[i][0], lst[i][1]))
