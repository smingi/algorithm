# 백준 15663_N과 M(9)


from itertools import permutations


N, M = map(int, input().split())  # N: N개의 자연수, M: 수열의 길이
numbers = list(map(int, input().split()))  # 사용할 수 있는 숫자
sequence = sorted(set(permutations(numbers, M)))  # N개의 자연수 중에서 M개를 고른 수열(사전순)

for seq in sequence:  # N개의 자연수 중에서 M개를 고른 수열(사전순) 출력
    for num in seq:
        print(num, end=" ")
    print()
