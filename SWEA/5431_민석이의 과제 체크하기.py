# 5431. 민석이의 과제 체크하기

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N: 전체 학생수 K: 제출한 학생수
    lst = list(map(int, input().split()))  # 제출한 명단

    result = []  # 안낸사람 리스트
    for i in range(N):
        if i+1 not in lst:  # 리스트에 없으면 입력
            result.append(i+1)
        if len(result) == (N - K):  # 안낸사람 다 찾으면 종료
            break

    print('#{}'.format(tc), end=' ')
    for i in range(len(result)):
        print(result[i], end=' ')
    print()
