# 백준 1208_부분수열의 합 2

import sys


def dfs(st, ed, num, dir):
    global cnt

    if st == ed:  # 하나만 남은 경우
        if dir == "l":  # 왼쪽인 경우 딕셔너리에 저장
            if num not in left_dic:
                left_dic[num] = 1
            else:
                left_dic[num] += 1

        elif S - num in left_dic:  # 오른쪽이면서 S를 만들수 있는 경우 개수 추가
            cnt += left_dic[S - num]

        return  # 종료

    dfs(st+1, ed, num+numbers[st], dir)  # 숫자 더해서 이동
    dfs(st+1, ed, num, dir)  # 그대로 이동


N, S = map(int, sys.stdin.readline().split())  # N: 정수의 개수, S: 정수
numbers = list(map(int, sys.stdin.readline().split()))  # 주어진 정수(절댓값으로 100000을 넘지 않음)
cnt = 0  # 합이 S가 되는 부분수열의 개수
left_dic = dict()  # 왼쪽 부분 (합: 개수)

dfs(0, N//2, 0, "l")  # 왼쪽
dfs(N//2, N, 0, "r")  # 오른쪽

if S == 0:  # S가 0인경우 두번세기 때문에 1번 빼기
    cnt -= 1

print(cnt)
