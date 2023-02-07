# 백준 4358_생태학

import sys


dic = dict()  # 나무별 개수
while True:
    tree = sys.stdin.readline().rstrip()  # 나무 이름

    if not tree:
        break

    if tree not in dic:
        dic[tree] = 1

    else:
        dic[tree] += 1

tree_list = [key for key in dic.keys()]  # 나무의 이름 오름차순
tree_list.sort()
total_tree = sum([value for value in dic.values()])  # 모든 나무의 개수

for tree in tree_list:
    print("{0} {1:.4f}".format(tree, dic[tree] / total_tree * 100))
