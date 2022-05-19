# 백준 1057 토너먼트


def binary(N, A, B):
    round = 1  # 현재 라운드

    while N:
        if (A+1)//2 == (B+1)//2:  # 만나서 경기를 하면 종료
            break
        else:  # 못 만나면 다음 라운드로 이동, 번호 변경
            A = (A+1)//2
            B = (B+1)//2
            round += 1
            N //= 2  # 경기가 진행될때마다 사람이 절반으로 줄어듬

    if not N:  # 못만나고 끝나면 -1
        return -1
    return round  # 만나고 끝나면 round 반환


N, A, B = map(int, input().split())  # N: 사람수, A: 사람1, B: 사람2
result = binary(N, A, B)  # 이진검색

print(result)
