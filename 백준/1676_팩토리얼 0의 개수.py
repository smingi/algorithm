# 백준 1676_팩토리얼 0의 개수


N = int(input())

factorial = 1  # 팩토리얼 계산 결과

for i in range(N, 1, -1):
    factorial *= i


check = list(str(factorial))  # 확인해야 하는 수
check.reverse()  # 계산하기 편하게 변경

for i in range(len(check)):
    if check[i] != "0":  # 0이 아니면 중단
        print(i)
        break
