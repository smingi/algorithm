# 백준 1992_쿼드트리


def compress(r, c, width):
    global compression
    color = screen[r][c]  # 현재 색
    check = True  # 조건 체크

    for i in range(r, r+width):
        for j in range(c, c+width):
            if screen[i][j] != color:  # 조건에 일치하지 않는 경우
                check = False
                break

    if check:  # 조건에 맞는 경우
        compression += str(color)

    else:  # 조건에 맞지 않는 경우
        compression += "("
        semi_width = width // 2
        for i in range(2):
            for j in range(2):
                compress(r + i * semi_width, c + j * semi_width, semi_width)
        compression += ")"


N = int(input())  # N*N: 영상 크기
screen = [list(map(int, input())) for _ in range(N)]

compression = ""  # 압축된 상태
compress(0, 0, N)  # 압축

print(compression)
