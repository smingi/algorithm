# 백준 9328_열쇠

import sys
from collections import deque


def bfs():
    q = deque()
    document = 0  # 찾은 문서
    block_entrance = deque()  # 막힌 입구
    visited = [[0] * w for _ in range(h)]  # 방문 여부

    # 사용할 수 있는 입구 찾기
    for r, c in entrance:
        if building[r][c].isalpha():  # 알파벳인 경우
            if building[r][c].islower():  # 소문자인 경우
                keys.append(building[r][c].upper())  # 열쇠 추가
                visited[r][c] = 1
                q.append([r, c])

            else:  # 대문자인 경우
                if building[r][c] in keys:  # 열쇠가 있으면 입구에 추가
                    visited[r][c] = 1
                    q.append([r, c])

                else:  # 열쇠가 없으면 막힌 입구로 저장
                    block_entrance.append([r, c])

        elif building[r][c] == "$":  # 문서를 찾은 경우
            document += 1
            visited[r][c] = 1
            q.append([r, c])

        else:  # 빈공간인 경우
            visited[r][c] = 1
            q.append([r, c])

    while q:
        r, c = q.popleft()  # 현재 위치

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and building[nr][nc] != "*":

                if building[nr][nc] == "$":  # 문서를 찾은 경우
                    document += 1
                    visited[nr][nc] = 1
                    q.append([nr, nc])

                elif building[nr][nc].isalpha():  # 알파벳인 경우
                    if building[nr][nc].islower():  # 소문자인 경우
                        keys.append(building[nr][nc].upper())  # 열쇠 추가
                        visited[nr][nc] = 1
                        q.append([nr, nc])

                        # 새로 들어갈 수 있는 입구 추가
                        for _ in range(len(block_entrance)):
                            br, bc = block_entrance.popleft()

                            if building[br][bc] in keys:  # 키가 있는 경우
                                visited[br][bc] = 1
                                q.append([br, bc])

                            else:  # 키가 없는 경우
                                block_entrance.append([br, bc])

                    else:  # 대문자인 경우
                        if building[nr][nc] in keys:  # 키가 있는 경우
                            visited[nr][nc] = 1
                            q.append([nr, nc])

                        else:  # 키가 없는 경우
                            block_entrance.append([nr, nc])

                else:  # 빈 공간인 경우
                    visited[nr][nc] = 1
                    q.append([nr, nc])

    return document


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())  # h: 높이, w: 너비
    building = [list(sys.stdin.readline().strip()) for _ in range(h)]
    # 빌딩정보 (.: 빈공간, *: 벽, $: 훔쳐야하는 문서, 알파벳 대문자: 문)
    keys = list(map(lambda x: x.upper(), sys.stdin.readline().strip()))  # 가지고 있는 열쇠 (대문자 문 = 소문자 열쇠)

    entrance = []  # 입구

    # 입구 찾기
    for i in range(h):
        for j in range(w):
            if (i == 0 or i == h-1 or j == 0 or j == w-1) and building[i][j] != "*":
                entrance.append([i, j])

    print(bfs())
