# 백준 1139_ATM


N = int(input())  # 사람수
lines = list(map(int, input().split()))  # 사람당 걸리는 시간

lines.sort()  # 오름차순으로 정렬
sumv = 0  # 총 걸리는 시간

for i in range(1, N+1):
    sumv += sum(lines[0:i])

print(sumv)
