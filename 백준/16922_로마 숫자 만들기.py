# 백준 16922 로마 숫자 만들기


def brute(n, cnt, sumv):
    if (cnt, sumv) in suml:  # 중복방지
        return
    else:
        suml.append((cnt, sumv))

    if cnt == n:  # n개면 중단
        if sumv not in lst:
            lst.append(sumv)
        return
    for i in [1, 5, 10, 50]:  # 탐색
        brute(n, cnt+1, sumv+i)


n = int(input())
lst = []  # 결과리스트
suml = []  # 중복방지 리스트
brute(n, 0, 0)  # 함수사용
print(len(lst))


