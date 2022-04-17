# 백준 6603 로또


def combi(idx, start):
    if idx == 6:  # 번호 6개 선택
        print(*sets)
        return

    for i in range(start, len(s)-5+idx):  # 조합
        sets[idx] = s[i]
        combi(idx+1, i+1)


while True:
    lst = list(map(int, input().split()))
    k = lst[0]  # 번호 개수
    s = lst[1:]  # 번호 리스트
    if k == 0:  # 종료조건
        break
    sets = [0] * 6  # 부분집합
    combi(0, 0)  # 조합사용
    print()
