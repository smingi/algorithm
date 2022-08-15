# 백준 1043_거짓말

import sys


N, M = map(int, input().split())  # N: 사람의 수, M: 파티의 수
truth = list(map(int, input().split()))  # 진실을 아는 사람의 수와 번호

mark = []  # 진실을 알게 된 사람 목록
for t in truth[1:]:
    mark.append(t)

party = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]  # 파티별 참여자 수와 번호
possible = [1] * M  # 거짓말을 할 수 있는 파티

idx = 0  # 인덱스
while idx < len(mark):
    for i in range(M):
        if possible[i] and mark[idx] in party[i][1:]:  # 거짓말을 할 수 있었는데, 진실을 아는 사람이 있는 경우
            possible[i] = 0  # 거짓말을 못하는 파티로 변경
            for p in party[i][1:]:
                if p not in mark:  # 진실을 새롭게 알게 된 사람을 목록에 추가
                    mark.append(p)
    idx += 1

print(sum(possible))  # 거짓말을 할 수 있는 파티 수
