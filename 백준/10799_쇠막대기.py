# 백준 10799_쇠막대기

import sys


bar = list(sys.stdin.readline().strip())  # 막대기 + 레이저
cnt = 0  # 막대기 개수
st = []

for i in range(len(bar)):
    if bar[i] == "(":
        st.append("(")

    else:
        if bar[i-1] == "(":
            st.pop()
            cnt += len(st)

        else:
            st.pop()
            cnt += 1

print(cnt)
