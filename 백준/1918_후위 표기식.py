# 백준 1918_후위 표기식


expression = list(input())  # 입력받은 식

st = []  # 스택
result = ""  # 결과

for e in expression:
    if e.isalpha():  # 기호가 아닌 경우
        result += e
    else:
        if e == "(":  # 여는 괄호
            st.append(e)
        elif e == "*" or e == "/":  # 곱셈, 나눗셈 처리
            while st and (st[-1] == "*" or st[-1] == "/"):
                result += st.pop()
            st.append(e)
        elif e == "+" or e == "-":  # 덧셈, 뺄셈 처리
            while st and st[-1] != "(":
                result += st.pop()
            st.append(e)
        elif e == ")":  # 닫는 괄호
            while st and st[-1] != "(":
                result += st.pop()
            st.pop()

while st:  # 남은 기호 처리
    result += st.pop()

print(result)
