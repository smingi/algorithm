# 백준 1991_트리 순회

import sys


def pre_order(k):  # 전위 순회
    if k != ".":
        print(k, end="")
        pre_order(dic[k][0])
        pre_order(dic[k][1])


def in_order(k):  # 중위 순회
    if k != ".":
        in_order(dic[k][0])
        print(k, end="")
        in_order(dic[k][1])


def post_order(k):  # 후위 순회
    if k != ".":
        post_order(dic[k][0])
        post_order(dic[k][1])
        print(k, end="")


N = int(input())  # 노드의 개수
dic = dict()
for _ in range(N):
    p, c1, c2 = sys.stdin.readline().split()  # p: 부모 노드, c1: 왼쪽 자식 노드, c2: 오른쪽 자식 노드
    dic[p] = [c1, c2]

pre_order("A")  # 전위 순회
print()  # 띄어쓰기
in_order("A")  # 중위 순회
print()  # 띄어쓰기
post_order("A")  # 후위 순회
