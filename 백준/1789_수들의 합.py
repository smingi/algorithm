#백준 1789 수들의 합

s = int(input())
sumv = 0 # 값들의 합
i = 1 # 정수
while sumv+i <= s:
    sumv += i
    i += 1

print(i-1)