# 백준 2357_최솟값과 최댓값

import sys
import math
sys.setrecursionlimit(10**6)


def segment_tree_init(left, right, node):  # 세그먼트 트리 생성
    if left == right:
        segment_tree[node] = [number[left], number[right]]
        return segment_tree[node]

    mid = (left + right) // 2
    left_side = segment_tree_init(left, mid, node*2)
    right_side = segment_tree_init(mid+1, right, node*2 + 1)
    segment_tree[node] = [min(left_side[0], right_side[0]), max(left_side[1], right_side[1])]

    return segment_tree[node]


def find(left, right, node):  # 원하는 범위 찾기
    # 검색이 불가능한 경우
    if left > b-1 or right < a-1:
        return [1000000000, 1]

    # 원하는 범위를 찾은 경우
    if left >= a-1 and right <= b-1:
        return segment_tree[node]

    mid = (left + right) // 2
    left_side = find(left, mid, node*2)
    right_side = find(mid+1, right, node*2 + 1)
    return [min(left_side[0], right_side[0]), max(left_side[1], right_side[1])]


N, M = map(int, sys.stdin.readline().split())  # N: 정수의 개수, M: 쌍의 개수
number = [int(sys.stdin.readline().strip()) for _ in range(N)]  # 주어진 정수
h = math.ceil(math.log2(N)) + 1  # 세그먼트 트리 높이 구하기
segment_tree = [[0, 0] for _ in range(1 << h)]  # 세그먼트 트리
segment_tree_init(0, N-1, 1)  # 세그먼트 트리 생성

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())  # a부터 b까지
    result = find(0, N-1, 1)  # 결과 [최솟값, 최댓값]
    print(result[0], result[1])
