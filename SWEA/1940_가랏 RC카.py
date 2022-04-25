# 1940. 가랏! RC카!

t = int(input())

for tc in range(1, t+1):
    command = int(input()) # 명령횟수
    distance = 0 # 이동거리
    speed = 0 # 이동속도
    for i in range(command):
        c = list(map(int, input().split()))
        if c[0] == 1: # 가속
            speed += c[1]
        elif c[0] == 2: # 감속
            speed -= c[1]
        if speed < 0: # 뒤로가기 방지
            speed = 0
        distance += speed
    print('#{} {}'.format(tc, distance))