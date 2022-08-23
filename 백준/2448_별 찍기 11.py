# 백준 2448_별 찍기 11


def make_star(start, end, n):
    if n <= 3:  # 마지막 부분인 경우 3층인 삼각형 만들기
        for i in range(3):
            for j in range(i+1):
                star[start+i][end+j] = "*"
                star[start+i][end-j] = "*"
        star[start+1][end] = " "
        return

    mid = n // 2
    make_star(start, end, mid)
    make_star(start + mid, end - mid, mid)
    make_star(start + mid, end + mid, mid)


N = int(input())  # N: 3 * 2^k
star = [[" "] * (N*2) for _ in range(N)]  # 별을 출력할 칸의 면적

make_star(0, N-1, N)  # 별 모양 만들기

for i in range(N):  # 출력
    print("".join(star[i]))
