# 백준 2529 부등호


def find(idx, num):
    if idx == K:  # 부호를 모두 사용하면 종료
        result.append(num)
        return

    for i in range(10):
        if not used[i]:  # 숫자 중복 방지
            if lst[idx] == '<':  # 조건 확인
                if int(num[-1]) > i:
                    continue
            else:
                if int(num[-1]) < i:
                    continue
            used[i] = 1
            find(idx+1, num+str(i))
            used[i] = 0


K = int(input())
lst = list(input().split())  # 입력받은 부등호 리스트
result = []  # 조건을 만족하는 숫자 리스트
for i in range(10):
    used = [0] * 10
    used[i] = 1
    find(0, str(i))

print(result[-1])
print(result[0])
