# 백준 2407_조합


n, m = map(int, input().split())  # nCm

numerator = n  # 분자
denominator = m  # 분모

for i in range(1, m):
    numerator *= n-i
    denominator *= i

print(numerator//denominator)
