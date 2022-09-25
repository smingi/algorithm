# 백준 11054_가장 긴 바이토닉 부분 수열


N = int(input())  # 수열의 길이
A = list(map(int, input().split()))  # 수열
R_A = list(A)  # 역 수열
R_A.reverse()

left = [1] * N  # 왼쪽 부분
right = [1] * N  # 오른쪽 부분
result = [0] * N  # 결과

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:  # 왼쪽
            left[i] = max(left[i], left[j] + 1)

        if R_A[i] > R_A[j]:  # 오른쪽
            right[i] = max(right[i], right[j] + 1)

for i in range(N):
    result[i] = left[i] + right[N-i-1] - 1

print(max(result))  # 최장 길이 출력
