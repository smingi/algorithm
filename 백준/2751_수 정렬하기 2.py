import sys

N = int(input())
lst = []

for i in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)

lst.sort()

for i in range(N):
    print(lst[i])
