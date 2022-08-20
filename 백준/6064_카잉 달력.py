# 백준 6064_카잉 달력


T = int(input())  # 테스트 케이스
for _ in range(T):
    M, N, x, y = map(int, input().split())

    not_found = True  # 발견 했는지 확인

    while x <= M * N:  # 최대 범위 이내일 때
        if x % N == y % N:  # x와 y 조건을 모두 충족한 경우
            print(x)
            not_found = False
            break

        x += M  # x 조건을 유지하기 위해 M을 더함

    if not_found:  # 끝까지 찾지 못한 경우
        print(-1)
