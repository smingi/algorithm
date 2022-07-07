# 백준 15686_치킨 배달


from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

home = []
store = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            store.append([i, j])

home_cnt = len(home)
result = 101 * home_cnt

for combi in combinations(store, M):
    min_distance = [101] * home_cnt
    for n_store in range(M):
        for n_home in range(home_cnt):
            temp_distance = abs(home[n_home][0] - combi[n_store][0]) + abs(home[n_home][1] - combi[n_store][1])
            if min_distance[n_home] > temp_distance:
                min_distance[n_home] = temp_distance

    if result > sum(min_distance):
        result = sum(min_distance)

print(result)
