# 백준 7568_덩치


N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    cnt = 1
    for j in range(N):
        if i != j and people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            cnt += 1

    print(cnt, end=" ")
