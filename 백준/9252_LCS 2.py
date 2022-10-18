# 백준_9252_LCS 2


word1 = [""] + list(input())  # 문장 1
word2 = [""] + list(input())  # 문장 2
dp = [[""] * len(word2) for _ in range(len(word1))]

for i in range(1, len(word1)):
    for j in range(1, len(word2)):
        if word1[i] == word2[j]:  # 일치하는 단어가 있는 경우
            dp[i][j] = dp[i-1][j-1] + word1[i]

        else:  # 일치하는 단어가 없는 경우 비교적 긴 단어 사용
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

result = dp[-1][-1]  # 찾은 LCS

if len(result) == 0:  # LCS 가 없는 경우
    print(0)

else:  # LCS 가 있는 경우
    print(len(result))
    print(result)
