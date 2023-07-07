# 백준 16566_카드 게임

import sys


def find_parent(x):  # 분리집합(부모노드 찾기)
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union(a, b):  # 분리집합(연결하기)
    if b < M:
        p_a = find_parent(a)
        p_b = find_parent(b)

        parent[p_a] = p_b


def find_idx(target):  # 이분탐색(주어진 수보다 큰 숫자의 인덱스 찾기)
    start, end = 0, M-1

    while start <= end:
        mid = (start + end) // 2

        if card[mid] <= target:
            start = mid + 1

        else:
            end = mid - 1

    return start


N, M, K = map(int, sys.stdin.readline().split())  # 1~N번 카드 , M: 뽑은 카드 개수, K: 비교 횟수
card = sorted(map(int, sys.stdin.readline().split()))  # 뽑은 카드 번호(오름차순)
cheol_su = list(map(int, sys.stdin.readline().split()))  # 철수가 내는 번호 순서
parent = [i for i in range(N+1)]  # 부모노드

for i in range(K):
    idx = find_idx(cheol_su[i])  # 주어진 수보다 큰 수 중에서 가장 작은 수의 인덱스
    idx = find_parent(idx)  # 주어진 수보다 크면서 사용되지 않은 가장 작은 수의 인덱스
    print(card[idx])
    union(idx, idx+1)  # 사용한 숫자 표시(다음에는 더 큰 숫자를 선택)
