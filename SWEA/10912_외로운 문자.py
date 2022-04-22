# 10912. 외로운 문자

t = int(input())
for tc in range(1, t+1):
    s = list(input())  # 문자열을 리스트로 입력받음
    s.sort()  # 리스트를 알파벳 순서로 정렬
    word = []
    i = 0
    while i < len(s):  # 비어있거나 다르면 넣고 같으면 뺀다.
        if len(word) and word[-1] != s[i]:
                word.append(s[i])
        elif len(word) and word[-1] == s[i]:
            word.pop()
        else:
            word.append(s[i])
        i += 1

    print('#{}'.format(tc), end=' ')
    if len(word):
        for i in range(len(word)):
            print(word[i], end='')
        print()
    else:
        print('Good')
