# 백준 15666_N과 M(12)


from itertools import combinations_with_replacement


N, M = map(int, input().split())  # N: 자연수의 개수, M: 수열의 길이
numbers = list(map(int, input().split()))  # 사용할 수 있는 자연수
numbers.sort()  # 오름차순으로 정렬

result = []

for seq in combinations_with_replacement(numbers, M):  # N개의 자연수 중에서 M개를 중복으로 고른 수열(비내림차순) 출력
    if seq not in result:
        result.append(seq)
        print(" ".join(map(str, seq)))
