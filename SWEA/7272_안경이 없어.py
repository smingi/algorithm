# 7272. 안경이 없어!

def compare(s1, s2):
    lst0 = list('CEFGHIJKLMNSTUVWXYZ')  # 구멍이 0개인 알파벳 리스트
    lst1 = list('ADOPQR')  # 구멍이 1개인 알파벳 리스트
    if len(s1) != len(s2): # 길이 다르면 다름
        return 'DIFF'
    else: # 길이가 같으면
        for i in range(len(s1)): # 같은 리스트에 있으면 같다고 판단 아니면 다르다고 판단
            if s1[i] in lst0 and s2[i] in lst0:
                continue
            elif s1[i] in lst1 and s2[i] in lst1:
                continue
            elif s1[i] == 'B' and s2[i] == 'B':
                continue
            else:
                return 'DIFF'
        return 'SAME'

t = int(input())
for tc in range(1, t+1):
    s1, s2 = input().split()
    print('#{} {}'.format(tc, compare(s1, s2)))

