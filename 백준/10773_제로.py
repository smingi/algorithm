# 백준 10773_제로


K = int(input())  # 정수 개수
st = []  # 스택

for _ in range(K):
    num = int(input())

    if num == 0:  # 문제에서 0일 경우 지울 수가 있다고 보장
        st.pop()
    else:
        st.append(num)

print(sum(st))
