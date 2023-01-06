# 백준 2257_화학식량

import sys


chemical_formula = sys.stdin.readline().strip()  # 화학식
dic = dict()
dic["H"] = 1  # 수소
dic["C"] = 12  # 탄소
dic["O"] = 16  # 산소
st = []

for c in chemical_formula:

    # 여는 괄호인 경우
    if c == "(":
        st.append(c)

    # 알파벳인 경우
    elif c in dic:
        st.append(dic[c])

    # 닫는 괄호인 경우
    elif c == ")":
        tmp = 0

        while True:
            now = st.pop()

            if now == "(":
                break

            tmp += now

        st.append(tmp)

    # 숫자인 경우
    else:
        st[-1] *= int(c)

print(sum(st))
