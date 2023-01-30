# 백준 1213_팰린드롬 만들기

import sys


word = sys.stdin.readline().strip()  # 입력받은 문자열
cnt = [0] * 26  # 알파벳의 개수
for w in word:
    cnt[ord(w) - ord("A")] += 1

odd = 0  # 홀수인 개수가 2개 이상이면 팰린드롬 불가
left = ""  # 왼쪽부분
mid = ""  # 중간부분
right = ""  # 오른쪽 부분

for i in range(26):

    # 홀수인 경우
    if cnt[i] % 2:
        odd += 1
        mid = chr(i + ord("A"))

        for j in range(cnt[i] // 2):
            left += chr(i + ord("A"))
            right = chr(i + ord("A")) + right

    # 짝수인 경우
    else:
        for j in range(cnt[i] // 2):
            left += chr(i + ord("A"))
            right = chr(i + ord("A")) + right

    # 팰린드롬을 만들 수 없는 경우
    if odd == 2:
        left = "I'm Sorry Hansoo"
        mid = ""
        right = ""
        break

print(left + mid + right)
