# 백준 9251_LCS


word1 = input()  # 1번 단어
word2 = input()  # 2번 단어

w1_len = len(word1)  # 1번 단어 길이
w2_len = len(word2)  # 2번 단어 길이

cnt = [[0] * (w2_len+1) for _ in range(w1_len+1)]  # 유사한 개수

for i in range(1, w1_len+1):  # 인덱스에러 방지용으로 1부터 1번 단어 길이+1
    for j in range(1, w2_len+1):  # 인덱스에러 방지용으로 1부터 2번 단어 길이+1
        if word1[i-1] == word2[j-1]:  # 일치 여부
            cnt[i][j] = cnt[i-1][j-1] + 1
        else:
            cnt[i][j] = max(cnt[i-1][j], cnt[i][j-1])

print(cnt[-1][-1])
