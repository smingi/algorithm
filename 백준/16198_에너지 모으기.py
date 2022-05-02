# 백준 16198 에너지 모으기


def get_maxv(sumv, marble):  # 완전탐색
    global energy
    if len(marble) == 2:  # 2개만 남으면 종료
        if sumv > energy:
            energy = sumv
        return

    for i in range(1, len(marble)-1):
        temp = marble[i]  # 빼는 값
        add = marble[i-1]*marble[i+1]  # 추가할 값
        marble.pop(i)  # 빼는 값 제거
        get_maxv(sumv + add, list(marble))  # 재귀
        marble.insert(i, temp)  # 원상복귀


N = int(input())
marbles = list(map(int, input().split()))
energy = 0  # 에너지
get_maxv(0, list(marbles))
print(energy)
