# 3499. 퍼펙트 셔플

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(input().split())
    m = n//2
    n_lst = []
    if n % 2:
        for i in range(m):
            n_lst.append(lst[i])
            n_lst.append(lst[i + m+1])
        n_lst.append(lst[m])
    else:
        for i in range(m):
            n_lst.append(lst[i])
            n_lst.append(lst[i + m])
    print('#{}'.format(tc), end=' ')
    for i in range(len(n_lst)):
        print(n_lst[i], end=' ')
    print()
