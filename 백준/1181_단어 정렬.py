# 백준 1181 단어 정렬


N = int(input())
lst = [input() for _ in range(N)]

lst = list(set(lst))
lst.sort()
lst.sort(key=len)

for word in lst:
    print(word)

