# 배준 2941 크로아티아 알파벳

s = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = [0] * len(lst)
for i in range(len(lst)):
    cnt[i] = s.count(lst[i])
result = len(s)
cnt[7] -= cnt[2]
for i in range(len(lst)):
    result -= (len(lst[i])-1) * cnt[i]
print(result)