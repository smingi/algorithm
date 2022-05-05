# 10947. 카나페


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    biscuit = list(map(int, input().split()))
    ingredient = list(map(int, input().split()))
    biscuit.sort(reverse=True)
    ingredient.sort(reverse=True)
    sumv = 0
    for i in range(N):
        sumv += biscuit[i] * ingredient[i]
    print('#{} {}'.format(tc, sumv))
