# 4659 비밀번호 발음하기

def pw(s):
    lst = ['a', 'e', 'i', 'o', 'u']
    s = list(s)
    cnt = 0
    for i in range(len(lst)):
        if lst[i] in s:
            cnt += 1
    if cnt == 0:
        return 0
    for i in range(len(s)-2):
        if s[i] in lst and s[i+1] in lst and s[i+2] in lst:
            return 0
        if s[i] not in lst and s[i+1] not in lst and s[i+2] not in lst:
            return 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            if s[i] == 'e' or s[i] == 'o':
                continue
            else:
                return 0
    return 1

s = ''
while s != 'end':
    s = input()
    if s == 'end':
        break
    if pw(s):
        print('<{}> is acceptable.'.format(s))
    else:
        print('<{}> is not acceptable.'.format(s))