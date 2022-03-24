# 4371. 항구에 들어오는 배

T = int(input())  # 테스트 케이스
for tc in range(1, T+1):
    N = int(input())  # 즐거운 날
    lst = [int(input()) for _ in range(N)]
    r_lst = []  # 주기 리스트
    n_lst = []  # 주기별로 리스트 채우기

    for i in range(1, len(lst)):
        if lst[i] in n_lst:  # 이미 체크했으면 이어서
            continue

        dif = lst[i] - lst[0]  # 시작일과 각 날짜의 차이
        tmp = dif + 1  # 처음값은 1을 더해야됨
        r_lst.append(dif)  # 주기 저장
        while tmp <= lst[-1]:
            if tmp in lst:
                n_lst.append(tmp)  # 주기에 포함된 것 체크
            tmp += dif  # 등차수열 이용

    print('#{} {}'.format(tc, len(r_lst)))
