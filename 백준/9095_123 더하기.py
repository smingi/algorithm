# 백준 9095 1, 2, 3 더하기


# DFS로 풀기
def dfs(sumv):
    if sumv > 10:  # 10이하일 때까지만 반복
        return
    box[sumv] += 1  # 개수 세기
    for i in range(1, 4):  # 1 ~ 3 더하기
        dfs(sumv+i)


box = [0] * 11  # 개수 리스트
dfs(0)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(box[N])


# DP로 풀기
box = [0] * 11  # 개수 리스트
box[1] = 1
box[2] = 2
box[3] = 4
for i in range(4, 11):
    box[i] = box[i-1] + box[i-2] + box[i-3]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(box[N])

