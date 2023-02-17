# 백준 2607_비슷한 단어

import sys


n = int(sys.stdin.readline().strip())  # 단어의 수
target = list(sys.stdin.readline().strip())  # 찾는 단어
result = 0

for _ in range(n-1):
    word = list(sys.stdin.readline().strip())  # 비교할 단어
    tmp_target = list(target)
    cnt = 0

    for w in word:
        if w in tmp_target:
            tmp_target.remove(w)
        else:
            cnt += 1

    if cnt <= 1 and len(tmp_target) <= 1:
        result += 1

print(result)
