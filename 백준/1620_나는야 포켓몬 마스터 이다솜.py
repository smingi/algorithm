# 백준 1620_나는야 포켓몬 마스터 이다솜

import sys


N, M = map(int, input().split())  # N: 포캣몬 수, M: 맞춰야 하는 문제의 개수
dic = dict()

for i in range(1, N+1):  # 도감 항목 저장
    name = sys.stdin.readline().strip()  # 포켓몬 이름(도감순)
    dic[name] = i  # (이름: 번호)저장
    dic[str(i)] = name  # (번호: 이름)저장

for _ in range(M):  # 문제 풀기
    question = sys.stdin.readline().strip()  # 문제
    print(dic[question])
