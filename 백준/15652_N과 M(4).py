# 백준 15652_N과 M(4)


def sequence(k):  # 중복으로 M개를 고른 순열(비내림차순)
    if len(selected) == M:
        print(" ".join(map(str, selected)))
        return

    for i in range(k, N+1):
        selected.append(i)
        sequence(i)
        selected.pop()


N, M = map(int, input().split())  # N: 1 ~ N 까지의 자연수, M: 수열의 길이
selected = []  # 선택한 숫자
sequence(1)  # 중복으로 M개를 고른 순열(비내림차순) 출력
