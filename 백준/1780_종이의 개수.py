# 백준 1780_종이의 개수


def find_cnt(r, c, width):
    global cnt_lst
    num = paper[r][c]  # 현재 종이에 써져 있는 숫자
    check = True  # 조건 확인

    for i in range(r, r+width):
        for j in range(c, c+width):
            if paper[i][j] != num:  # 조건에 맞지 않는 경우
                check = False
                break

    if check:  # 조건에 맞으면 개수 추가
        cnt_lst[num+1] += 1

    else:  # 조건에 맞지 않으면 분할 탐색
        tri_width = width//3  # 3등분
        for i in range(3):
            for j in range(3):
                find_cnt(r + tri_width * i, c + tri_width * j, tri_width)


N = int(input())  # N*N: 종이 크기
paper = [list(map(int, input().split())) for _ in range(N)]  # 종이 상태

cnt_lst = [0] * 3  # 각 숫자로 이루어진 종이의 개수
find_cnt(0, 0, N)

for cnt in cnt_lst:  # 개수 출력
    print(cnt)
