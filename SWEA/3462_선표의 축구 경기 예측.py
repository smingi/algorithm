# swea 3462 선표의 축구 경기 예측


p_num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # 소수
combination = [0] * len(p_num)  # 조합
for i in range(len(p_num)):
    combi = 1  # 30개 중 p_num[i]개 뽑기
    for j in range(30, 30 - p_num[i], -1):
        combi *= j
    for j in range(1, p_num[i] + 1):
        combi /= j
    combination[i] = combi

T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    a_goal = A / 100  # a팀이 골 넣을 확률
    a_ngoal = 1 - a_goal  # a팀이 골 못 넣을 확률
    b_goal = B / 100
    b_ngoal = 1 - b_goal
    a = 0  # a팀이 소수로 골을 넣을 확률
    b = 0
    for i in range(len(p_num)):
        a_per = (a_goal ** p_num[i]) * (a_ngoal ** (30 - p_num[i]))  # a팀 확률
        b_per = (b_goal ** p_num[i]) * (b_ngoal ** (30 - p_num[i]))
        a += a_per * combination[i]  # a팀이 i(소수)개 넣을 확률
        b += b_per * combination[i]
    result = 1 - (1 - a) * (1 - b)  # 1 - (a, b 팀 둘다 소수로 못넣을 확률)
    print('#{0} {1:.5f}'.format(tc, result))
