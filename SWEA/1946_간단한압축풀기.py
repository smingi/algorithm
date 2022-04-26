# 1946. 간단한 압축 풀기

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc))
    n = int(input())
    s = 'x'
    for _ in range(n): # 출력하는 문자열을 하나로 만들기
        a, num = input().split()
        s += a*int(num)

    for i in range(1, len(s)): # 필요한 방식으로 출력
        print(s[i], end='')
        if i%10 == 0:
            print()
    print()