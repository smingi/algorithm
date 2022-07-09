# 백준 2661 좋은수열


def check(check_str):
    for i in range(2, len(check_str) // 2 + 1):
        for j in range(i, len(check_str) - i + 1):
            if check_str[j - i:j] == check_str[j:j + i]:
                return False

    return True


def dfs():
    global result, stop
    if stop:
        return

    if len(result) == N:
        print(result)
        stop = True
        return

    for num in ["1", "2", "3"]:
        if result[-1] != num and check(result + num):
            result += num
            dfs()
            result = result[:len(result)-1]


N = int(input())
stop = False
result = "1"
dfs()
