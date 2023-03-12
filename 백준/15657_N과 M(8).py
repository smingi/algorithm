# 백준 15657_N과 M(8)


def sequence(k):  # N개의 자연수 중에서 M개를 중복으로 고른 수열(비내림차순)
    if len(selected) == M:
        print(" ".join(map(str, selected)))
        return

    for i in range(k, N):
        selected.append(numbers[i])
        sequence(i)
        selected.pop()


N, M = map(int, input().split())  # N: 자연수 개수, M: 수열의 길이
numbers = list(map(int, input().split()))  # 사용할 수 있는 숫자
numbers.sort()  # 오름차순으로 정렬
selected = []  # 선택한 숫자
sequence(0)  # N개의 자연수 중에서 M개를 중복으로 고른 수열(비내림차순) 출력
