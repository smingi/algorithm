# 2164_카드2


from collections import deque


N = int(input())
numbers = deque([i for i in range(1, N+1)])

while True:
    if len(numbers) == 1:
        break

    numbers.popleft()
    num = numbers.popleft()
    numbers.append(num)

print(numbers[0])
