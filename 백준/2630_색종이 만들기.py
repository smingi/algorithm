# 백준 2630 색종이 만들기


def check_paper(r, c, width):
    global white, blue

    now_color = paper[r][c]  # 현재 시작점 색
    semi_width = width // 2  # 절반 길이

    for i in range(r, r+width):
        for j in range(c, c+width):
            if paper[i][j] != now_color:  # 색이 다른 부분이 있으면 분할
                check_paper(r, c, semi_width)  # 1사분면
                check_paper(r, c + semi_width, semi_width)  # 2사분면
                check_paper(r + semi_width, c, semi_width)  # 3사분면
                check_paper(r + semi_width, c + semi_width, semi_width)  # 4사분면
                return

    if now_color:  # 1이면 파란색 0이면 흰색
        blue += 1
    else:
        white += 1


N = int(input())  # N*N의 종이
paper = [list(map(int, input().split())) for _ in range(N)]  # 색칠된 종이 상태

white = 0  # 흰색 종이 개수
blue = 0  # 파란 종이 개수
check_paper(0, 0, N)  # 분할 탐색

print(white)
print(blue)
