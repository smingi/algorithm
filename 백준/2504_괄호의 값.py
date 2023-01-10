# 백준 2504_괄호의 값

import sys


bracket = sys.stdin.readline().strip()  # 괄호
st = []
tmp = 1
result = 0

for i in range(len(bracket)):

    # 여는 괄호 1
    if bracket[i] == "(":
        tmp *= 2
        st.append(bracket[i])

    # 여는 괄호 2
    elif bracket[i] == "[":
        tmp *= 3
        st.append(bracket[i])

    # 닫는 괄호 1
    elif bracket[i] == ")":

        # 올바르지 않은 괄호
        if not st or st[-1] == "[":
            result = 0
            break

        # 올바른 괄호
        if bracket[i-1] == "(":
            result += tmp

        st.pop()
        tmp //= 2

    # 닫는 괄호 2
    elif bracket[i] == "]":

        # 올바르지 않은 괄호
        if not st or st[-1] == "(":
            result = 0
            break

        # 올바른 괄호
        if bracket[i - 1] == "[":
            result += tmp

        st.pop()
        tmp //= 3

if st:
    print(0)

else:
    print(result)
