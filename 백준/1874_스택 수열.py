# 백준 1874_스택 수열


N = int(input())
lst = [int(input()) for _ in range(N)]

st = []
now = 1
push_pop = []

while True:
    if (st and st[-1] > N) or not lst:
        break

    if not st:
        st.append(now)
        now += 1
        push_pop.append("+")

    elif lst[0] == st[-1]:
        lst.pop(0)
        st.pop()
        push_pop.append("-")

    elif lst[0] > st[-1]:
        st.append(now)
        now += 1
        push_pop.append("+")

    elif lst[0] < st[-1]:
        st.pop()
        push_pop.append("-")


if lst:
    print("NO")
else:
    for calc in push_pop:
        print(calc)

