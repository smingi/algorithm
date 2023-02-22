# 백준 3986_좋은 단어

import sys


N = int(sys.stdin.readline().strip())  # 단어의 수
result = 0
for _ in range(N):
    word = sys.stdin.readline().strip()
    st = []

    for w in word:
        if not st:
            st.append(w)

        elif st[-1] == w:
            st.pop()

        else:
            st.append(w)

    if not st:
        result += 1

print(result)
