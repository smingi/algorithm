# 백준 10816_숫자 카드2


N = int(input())
n_lst = list(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

dic = dict()

for n_num in n_lst:
    if n_num in dic:
        dic[n_num] += 1
    else:
        dic[n_num] = 1

for m_num in m_lst:
    if m_num in dic:
        print(dic[m_num], end=" ")
    else:
        print(0, end=" ")
