# swea 1248 공통조상


def find_subtree(x):  # 서브트리 찾는 함수
    q = []
    q.append(x)
    while q:
        x = q.pop(0)
        for i in range(1, V+1):
            if p[i] == x and i not in subtree:
                q.append(i)
                subtree.append(i)


def find_p(x):  # 가까운 공통 조상노드 찾는 함수
    lst.append(x)
    while x != p[x]:
        x = p[x]
        if x in lst:
            return x
        lst.append(x)
    return lst


T = int(input())
for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())  # V: 정점 총 개수, E: 간선 총 개수, A, B: 비교대상
    edges = list(map(int, input().split()))  # 간선 정보
    p = [i for i in range(V+1)]  # 부모노드 정보
    for i in range(0, len(edges), 2):
        p[edges[i+1]] = edges[i]
    lst = []  # 공통 조상노드로 가는 노드 리스트
    A_lst = find_p(A)
    result = find_p(B)  # 공통 조상노드
    subtree = [result]  # 서브트리 저장 리스트
    find_subtree(result)
    print('#{} {} {}'.format(tc, result, len(subtree)))
