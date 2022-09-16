# 백준 1932_정수 삼각형


n = int(input())  # n: 삼각형의 크기
lst = [list(map(int, input().split())) for _ in range(n)]  # 정수 삼각형

for i in range(1, n):  # 내려가면서 계산
    for j in range(len(lst[i])):
        if j == 0:  # 왼쪽 끝부분
            lst[i][j] += lst[i-1][j]
        elif j == i:  # 오른쪽 끝부분
            lst[i][j] += lst[i-1][j-1]
        else:  # 중간 부분
            lst[i][j] += max(lst[i-1][j], lst[i-1][j-1])

print(max(lst[n-1]))
