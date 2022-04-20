# 백준 10158 개미

w, h = map(int, input().split())  # 가로, 새로
x, y = map(int, input().split())  # x축, y축
t = int(input())  # 시간

w_lst = [i for i in range(w)] + [j for j in range(w, 0, -1)]  # 가로 리스트
h_lst = [i for i in range(h)] + [j for j in range(h, 0, -1)]  # 새로 리스트

nx_idx = (w_lst.index(x) + t) % len(w_lst)  # 이동한 가로축의 인덱스
ny_idx = (h_lst.index(y) + t) % len(h_lst)  # 이동한 세로축의 인덱스
nx = w_lst[nx_idx]  # 이동한 가로축 위치
ny = h_lst[ny_idx]  # 이동한 세로축 위치
print(nx, ny)