# 백준 16165_걸그룹 마스터 준석이

import sys


N, M = map(int, sys.stdin.readline().split())  # N: 걸그룹의 수, M: 맞춰야할 문제수
dic = dict()
for _ in range(N):
    group_name = sys.stdin.readline().strip()  # 걸그룹 이름
    group_cnt = int(sys.stdin.readline().strip())  # 걸그룹 맴버 수
    group_lst = []

    for _ in range(group_cnt):
        name = sys.stdin.readline().strip()  # 맴버 이름
        dic[name] = group_name
        group_lst.append(name)

    group_lst.sort()
    dic[group_name] = group_lst

for _ in range(M):
    question = sys.stdin.readline().strip()  # 문제
    question_type = int(sys.stdin.readline().strip())  # 문제 타입

    if question_type == 1:
        print(dic[question])

    elif question_type == 0:
        for answer in dic[question]:
            print(answer)
