# 백준 15650_N과 M(2)


def sequence(k):  # 중복 없이 M개를 고른 순열(오름차순)
    if len(selected) == M:
        print(" ".join(map(str, selected)))
        return

    for i in range(k, N+1):
        if i not in selected:
            selected.append(i)
            sequence(i+1)
            selected.pop()


N, M = map(int, input().split())  # N: 1 ~ N 까지의 자연수, M: 수열의 길이
selected = []  # 선택한 숫자
sequence(1)  # 조건에 맞는 수열 출력
