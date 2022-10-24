# 백준 11866_요세푸스 문제0


N, K = map(int, input().split())

numbers = [i for i in range(1, N+1)]
index = K-1

print("<", end="")
for i in range(N):
    num = numbers.pop(index)
    if i == N-1:
        print("{}>".format(num))
    else:
        print(num, end=", ")

    if numbers:
        index = (index + K - 1) % len(numbers)
