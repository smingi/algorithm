# 백준 4949_균형잡힌 세상


while True:
    words = list(input())  # 입력받은 문자열

    if words[0] == ".":  # 종료 조건
        break

    left = []  # 여는 부분 리스트
    for word in words:
        if word == "(" or word == "[":  # 여는 부분
            left.append(word)

        elif word == ")":  # 닫는 부분1
            if left and left[-1] == "(":
                left.pop()
            else:
                left.append(word)
                break

        elif word == "]":  # 닫는 부분2
            if left and left[-1] == "[":
                left.pop()
            else:
                left.append(word)
                break

    if left:  # 남아 있는 괄호가 있으면 no 없으면 yes
        print("no")
    else:
        print("yes")
