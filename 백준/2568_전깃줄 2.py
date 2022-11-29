# 백준 2568 전깃줄 - 2

import sys
import bisect


n = int(sys.stdin.readline().strip())  # 전깃줄의 개수
line = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 전깃줄 (a <-> b)
line.sort()  # 왼쪽 전봇대를 기준으로 오름차순으로 정렬
dp = [0] * n
lst = [-1]

# 오른쪽 전봇대에서 가장 긴 증가하는 수열 찾기
for i in range(n):
    if line[i][1] > lst[-1]:
        lst.append(line[i][1])
        dp[i] = len(lst) - 1

    else:
        dp[i] = bisect.bisect_left(lst, line[i][1])
        lst[dp[i]] = line[i][1]

max_v = max(dp)  # 오른쪽 전봇대에서 가장 긴 증가하는 수열의 길이
result = []  # 오른쪽 전봇대에서 가장 긴 증가하는 수열에 포함되지 않는 전깃줄의 번호(왼쪽 전봇대 기준)

for i in range(n-1, -1, -1):
    if dp[i] == max_v:  # 증가하는 수열에 포함되는 경우
        max_v -= 1

    else:  # 증가하는 수열에 포함되지 않는 경우
        result.append(line[i][0])

# 없애야 하는 전깃줄의 최소 개수
print(len(result))

# 없애야 하는 전깃줄의 번호(왼쪽 전봇대 기준 오름차순)
for r in result[::-1]:
    print(r)
