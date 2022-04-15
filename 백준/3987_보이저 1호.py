# 백준 3987 보이저 1호


def travel(dir):
    global maxv, direction, stopper
    q = []
    time = 0
    if dir == 'U':  # 위
        q.append((PR - 1, PC - 1, -1, 0, time))
    elif dir == 'R':  # 오른족
        q.append((PR-1, PC-1, 0, 1, time))
    elif dir == 'D':  # 아래
        q.append((PR-1, PC-1, 1, 0, time))
    else:  # 왼쪽
        q.append((PR-1, PC-1, 0, -1, time))

    while q:
        cr, cc, dr, dc, time = q.pop(0)
        if cr < 0 or cr >= N or cc < 0 or cc >= M or lst[cr][cc] == 'C':  # 범위 탐지
            if maxv < time:
                maxv = time
                direction = dir
            return
        if time > M*N*2:  # 무한루프 탐지
            direction = dir
            stopper = 'Voyager'
            return

        elif lst[cr][cc] == '/':
            ndr = dc * -1
            ndc = dr * -1
        elif lst[cr][cc] == '.':
            ndr = dr
            ndc = dc
        else:
            ndr = dc
            ndc = dr
        q.append((cr+ndr, cc+ndc, ndr, ndc, time+1))


N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
PR, PC = map(int, input().split())
direction = ''  # 방향
maxv = 0  # 최대값
stopper = ''  # 무한루프

travel('U')
if not stopper:
    travel('R')
if not stopper:
    travel('D')
if not stopper:
    travel('L')
print(direction)
if stopper:
    print(stopper)
else:
    print(maxv)

