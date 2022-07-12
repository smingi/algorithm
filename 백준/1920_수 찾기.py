# 1920_수 찾기


N = int(input())
n_lst = list(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

n_lst.sort()

for m_num in m_lst:
    st = 0
    ed = N-1
    printed = False

    while st <= ed:
        mid = (st+ed)//2
        if m_num == n_lst[mid]:
            print(1)
            printed = True
            break
        elif m_num > n_lst[mid]:
            st = mid + 1
        else:
            ed = mid - 1

    if not printed:
        print(0)
