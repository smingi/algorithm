# 백준 11899_괄호 끼워넣기

import sys


S = sys.stdin.readline().strip()  # 괄호
st = []

for s in S:
    if not st:
        st.append(s)

    elif s == ")" and st[-1] == "(":
        st.pop()

    else:
        st.append(s)

print(len(st))
