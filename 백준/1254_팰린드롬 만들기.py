# 백준 1254 팰린드롬 만들기


S = list(input())
result = list(S)

for i in range(len(S)):
    if S[i:] == list(reversed(S[i:])):
       result += S[0:i][::-1]
       break

print(len(result))
