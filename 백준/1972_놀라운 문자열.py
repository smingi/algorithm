# 백준 1972_놀라운 문자열

import sys


# 조건 체크
def check(w):
    for distance in range(len(w) - 1):
        result = set()

        for i in range(len(w) - 1 - distance):
            pair = w[i] + w[i+distance+1]

            if pair in result:
                return False

            else:
                result.add(pair)

    return True


while True:
    # 입력받은 문자열
    word = sys.stdin.readline().strip()

    # 종료조건
    if word == '*':
        break

    # 조건 체크
    if check(word):
        print(word, 'is surprising.')

    else:
        print(word, 'is NOT surprising.')
