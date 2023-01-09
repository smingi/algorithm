# 2493_탑

import sys


N = int(sys.stdin.readline().strip())  # 탑의 개수
tower = list(map(int, sys.stdin.readline().split()))  # 탑의 높이
result = [0] * N  # 결과
st = []

for i in range(len(tower)):

    # 스택에 값이 있는 경우, 스택 맨 뒤의 값이 현재 탑의 높이보다 크거나 같을 때까지 값을 빼기
    while st and st[-1][0] < tower[i]:
        st.pop()

    # 스택에 값이 있는 경우, 스택 맨 뒤의 값의 인덱스를 결과에 넣기
    if st:
        result[i] = st[-1][1]

    # 스택에 새로운 값 넣기(탑의 높이, 탑의 인덱스)
    st.append([tower[i], i+1])

print(" ".join(map(str, result)))
