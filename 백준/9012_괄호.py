# 백준 9012_괄호


n = int(input())
for _ in range(n):
    lst = list(input())
    st = []
    result = "YES"

    for ps in lst:
        if ps == "(":
            st.append(ps)
        elif ps == ")" and st:
            st.pop()
        else:
            result = "NO"
            break

    if st:
        result = "NO"

    print(result)
