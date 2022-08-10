# 백준 2263_트리의 순회

import sys
sys.setrecursionlimit(10**6)


def pre_order(in_st, in_ed, post_st, post_ed):
    if in_st > in_ed or post_st > post_ed:  # 범위 초과 방지
        return

    root = post_order[post_ed]
    print(root, end=" ")

    root_index = index_dic[root]  # 현재 위치 인덱스
    left = root_index - in_st  # 왼쪽 부분
    right = in_ed - root_index  # 오른쪽 부분

    pre_order(in_st, root_index - 1, post_st, post_st + left - 1)  # 왼쪽 부분
    pre_order(root_index + 1, in_ed, post_ed - right, post_ed - 1)  # 오른쪽 부분


n = int(input())  # 정점 개수
in_order = list(map(int, input().split()))  # 인 오더 방식
post_order = list(map(int, input().split()))  # 포스트 오더 방식

index_dic = dict()  # 중위 순회 각각의 값의 인덱스값 저장
for i in range(n):  # ex) 예제 입력 1을 기준으로 1은 0번 인덱스, 2는 1번 인덱스, 3은 2번 인덱스
    index_dic[in_order[i]] = i

pre_order(0, n-1, 0, n-1)  # 프리오더 방식
