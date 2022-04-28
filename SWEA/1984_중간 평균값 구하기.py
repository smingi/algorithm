# 1984. 중간 평균값 구하기

n = int(input())

def max_min(lst):
    maxv = 0
    minv = 10001
    for l in lst:
        if l > maxv:
            maxv = l
        if l < minv:
            minv = l
    return maxv,minv

for tc in range(n):
    lst = list(map(int, input().split()))
    total = 0
    for i in lst:
        total += i
    maxv, minv = max_min(lst)
    avg = round((total - maxv - minv)/(len(lst)-2))
    print('#{0} {1}'.format(tc+1,avg))