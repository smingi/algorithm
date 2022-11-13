# 백준 1509_팰린드롬 분할

import sys


words = sys.stdin.readline().strip()  # 주어진 문자열
length = len(words)  # 문자열의 길이
dp = [[0] * length for _ in range(length)]  # 팰린드롬 여부

# 팰린드롬 여부 파악
# 길이가 1일때
dp[length-1][length-1] = 1
for i in range(length-1):
    dp[i][i] = 1

    # 길이가 2일때
    if words[i] == words[i+1]:
        dp[i][i+1] = 1

# 길이가 3 이상일 때
for cnt in range(2, length):
    for start in range(length-cnt):
        end = start + cnt

        if words[start] == words[end] and dp[start+1][end-1]:
            dp[start][end] = 1

min_length = [2500] * (length+1)  # 최소길이(최대 2500)
min_length[length] = 0

# 팰린드롬 최소 분할 개수 파악
for end in range(length):
    for start in range(end+1):
        if dp[start][end]:  # words[start:end+1]가 팰린드롬인 경우
            min_length[end] = min(min_length[end], min_length[start-1] + 1)
        else:  # 팰린드롬이 아닌 경우
            min_length[end] = min(min_length[end], min_length[end-1] + 1)

print(min_length[length-1])  # 팰린드롬 분할 개수의 최솟값
