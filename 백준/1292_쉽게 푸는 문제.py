# 1292 쉽게 푸는 문제

lst = [0] # 수열 리스트
s, e = map(int, input().split())
for i in range(1, 47):
    number = [i]*i
    lst += number
    
print(sum(lst[s:e+1]))
