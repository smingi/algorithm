# 백준 9935_문자열 폭발


words = input()  # 주어진 문자열
boom = input()  # 폭발 문자열
st = []  # 스택
b_length = len(boom)

for word in words:
    st.append(word)
    s_length = len(st)

    while s_length >= b_length and "".join(st[s_length-b_length: s_length]) == boom:
        # 폭발문자열이 있는 경우 반복해서 제거
        s_length = len(st)
        for _ in range(b_length):
            st.pop()

if st:
    print("".join(st))
else:
    print("FRULA")
