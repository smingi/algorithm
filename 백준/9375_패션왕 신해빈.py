# 백준 9375_패션왕 신해빈


T = int(input())  # 테스트 케이스
for _ in range(T):
    n = int(input())  # 가진 의상 수

    kinds = []  # 옷 종류
    dic = dict()  # 옷 종류별 개수

    for _ in range(n):
        name, kind = input().split()  # 가진 의상 이름 및 종류

        if kind not in kinds:
            kinds.append(kind)
            dic[kind] = 1

        else:
            dic[kind] += 1

    result = 1  # 결과
    for k in kinds:
        result *= dic[k]+1  # 옷 종류별 경우의 수

    result -= 1  # 모두 안 입는 경우 제외

    print(result)
