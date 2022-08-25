# 백준 5639_이진 검색 트리

import sys
sys.setrecursionlimit(10**6)


def post_order(start, end):  # 후위 순회
    if start > end:  # 종료지점
        return

    new_root = end + 1  # 새로운 중간지점 찾기

    for i in range(start+1, end+1):
        if pre_order[start] < pre_order[i]:
            new_root = i
            break

    post_order(start+1, new_root-1)  # 왼쪽 부분
    post_order(new_root, end)  # 오른쪽 부분

    print(pre_order[start])


pre_order = []  # 전위 순회

while True:
    try:
        num = int(sys.stdin.readline().strip())
        pre_order.append(num)

    except:
        break

post_order(0, len(pre_order)-1)  # 후위 순회
