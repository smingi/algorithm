# 백준 1935_후위 표기식2

import sys


def calc(a, b, oper):
    if oper == "+":
        return a + b

    elif oper == "-":
        return a - b

    elif oper == "*":
        return a * b

    elif oper == "/":
        return a / b


N = int(sys.stdin.readline().strip())  # 피연산자의 개수
expression = sys.stdin.readline().strip()  # 후위 표기식
value = [int(sys.stdin.readline().strip()) for _ in range(N)]
st = []

for e in expression:
    if 'A' <= e <= 'Z':
        st.append(value[ord(e) - ord('A')])

    else:
        b = st.pop()
        a = st.pop()
        st.append(calc(a, b, e))

print("{0:.2f}".format(st[0]))
