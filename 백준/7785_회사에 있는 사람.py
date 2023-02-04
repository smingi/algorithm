# 백준 7785_회사에 있는 사람

import sys


n = int(sys.stdin.readline().strip())  # 출입 기록의 수
in_person = dict()  # 안에 있는 사람 명단

for _ in range(n):
    name, status = sys.stdin.readline().split()  # 이름, 출입상태

    if status == "enter":
        if name not in in_person:
            in_person[name] = 1

        else:
            in_person[name] += 1

    else:
        if name in in_person:
            in_person[name] -= 1

result = [key for key in in_person.keys() if in_person[key] > 0]
result.sort(reverse=True)

for r in result:
    print(r)
