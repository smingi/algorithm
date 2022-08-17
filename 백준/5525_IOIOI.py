# 백준 5525_IOIOI


N = int(input())  # IOI 길이
M = int(input())  # 주어진 문자열(S)의 길이
S = input()  # 주어진 문자열

idx = 3  # 인덱스
cnt = 0  # 연속된 IOI 개수
result_cnt = 0  # 길이가 N인 IOI 개수

while idx <= M:  # 범위 내에서
    if S[idx-3:idx] == "IOI":  # IOI 를 발견하면
        cnt += 1  # 연속된 IOI 개수 +1
        if cnt == N:  # 길이가 N인 IOI 를 발견하면 결과 개수 +1, 연속된 IOI 개수 -1
            result_cnt += 1
            cnt -= 1
        idx += 2  # 두칸 이동

    else:  # IOI 가 아니면
        cnt = 0  # 연속된 IOI 개수 0으로 초기화
        idx += 1  # 한칸 이동

print(result_cnt)
