# 백준 4358


S = list(input())
result = list(S)

for i in range(len(S)):
    if S[i:] == list(reversed(S[i:])):
       result += S[0:i][::-1]
       break

print(len(result))
