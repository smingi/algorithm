# 백준 3584 가장 가까운 공통 조상


def find_p(x):  # 부모노드 찾는 함수
    lst = []
    lst.append(x)
    while x != p[x]:
        x = p[x]
        lst.append(x)
    return lst


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 노드 개수
    p = [i for i in range(N+1)]  # 부모노드 정보 리스트
    for _ in range(N-1):  # 부모노드 정보
        a, b = map(int, input().split())
        p[b] = a
    A, B = map(int, input().split())  # 비교대상 A, B
    A_lst = find_p(A)  # A 부모노드 리스트
    B_lst = find_p(B)  # B 부모노드 리스트
    result = 0  # 결과
    i = 0
    while i < len(A_lst):
        if A_lst[i] in B_lst:
            result = A_lst[i]
            break
        i += 1
    print(result)
