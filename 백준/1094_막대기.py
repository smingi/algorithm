# 백준 1094 막대기


bar_lst = []
number = 64
while number > 0:
    bar_lst.append(number)
    number //= 2

x = int(input())
result = 0
sumv = 0
for num in bar_lst:
    if sumv == x:
        break
    if sumv < x and sumv + num <= x:
        sumv += num
        result += 1

print(result)
