# 8016. 홀수 피라미드

t = int(input())
for tc in range(1, t+1):
    floor = int(input())
    start = 2 * ((floor-1)**2 + 1 ) - 1
    end = 2 * floor**2 - 1
    
    print('#{} {} {}'.format(tc, start, end))
