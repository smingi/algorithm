# 백준 15654_N과 M(5)


def sequence():  # N개의 자연수 중에서 M개를 고른 수열(사전순)
    if len(selected) == M:
        print(" ".join(map(str, selected)))
        return

    for i in range(N):
        if not visited[i]:
            selected.append(numbers[i])
            visited[i] = 1
            sequence()
            selected.pop()
            visited[i] = 0


N, M = map(int, input().split())  # N: 자연수 개수, M: 수열의 길이
numbers = list(map(int, input().split()))  # 사용할 수 있는 숫자
numbers.sort()  # 오름차순으로 정렬
visited = [0] * N
selected = []  # 선택한 숫자
sequence()  # N개의 자연수 중에서 M개를 고른 수열(사전순) 출력
