# 백준 1074_Z


N, r, c = map(int, input().split())  # N: 정수, r: 행위치, c: 열위치
order = 0  # 방문 순서

while N > 0:
    N -= 1  # 면적 감소
    width = 2**N  # 현재 길이
    area = width * width  # 분면당 넓이

    if r < width and c < width:  # 1사분면
        pass

    elif r < width <= c:  # 2사분면
        c -= width  # 열을 면적보다 작은 범위로 이동
        order += area  # 1사분면 면적 더하기

    elif r >= width > c:  # 3사분면
        r -= width  # 행을 면적보다 작은 범위로 이동
        order += area * 2  # 1, 2사분면 면적 더하기

    else:  # 4사분면
        c -= width  # 열을 면적보다 작은 범위로 이동
        r -= width  # 행을 면적보다 작은 범위로 이동
        order += area * 3  # 1, 2, 3사분면 면적 더하기

print(order)
