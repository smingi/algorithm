# 백준 1436_영화감독 숌


N = int(input())
number = 666
cnt = 0

while True:
    if "666" in str(number):
        cnt += 1

    if cnt == N:
        print(number)
        break

    number += 1
