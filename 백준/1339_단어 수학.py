# 백준 1339_단어 수학

import sys


N = int(sys.stdin.readline().strip())  # N: 단어의 수
dic = dict()

for _ in range(N):
    word = sys.stdin.readline().strip()  # 입력받은 단어
    length = len(word)  # 단어의 길이

    # 자릿수로 계산해서 알파벳 별로 비중을 계산
    for i in range(length):
        if word[i] in dic:
            dic[word[i]] += 10 ** (length - 1 - i)

        else:
            dic[word[i]] = 10 ** (length - 1 - i)

values = [value for value in dic.values()]  # 알파벳 별 비중
values.sort(reverse=True)  # 비중이 높은 순으로 정렬

# 비중이 높은 순으로 높은 숫자 배정 및 합산
result = 0
num = 9
for v in values:
    result += v * num
    num -= 1

print(result)
