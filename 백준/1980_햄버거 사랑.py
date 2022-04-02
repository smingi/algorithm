# 벡준 1980 햄버거 사랑

n, m, t = map(int, input().split())
if n > m:  # 시간 긴것과 짧은 것 찾기
    maxv = n
    minv = m
else:
    maxv = m
    minv = n

coke = t  # 콜라 마시는 시간
cnt = 0  # 시간 긴 버거의 개수
max_cnt = t // minv  # 최대 버거 개수
burger = 0  # 버거 개수
while coke > 0 and cnt <= max_cnt:  # coke가 0이 되거나 최대 개수가 안 넘을때까지 반복
    temp_burger = (t - (maxv * cnt)) // minv + cnt  # 버거값이 큰 값부터 찾기
    temp_coke = (t - (maxv * cnt)) % minv
    if t < (maxv * cnt):  # 음수를 나누는 것 방지
        break
    if temp_coke < coke:
        coke = temp_coke  # 콜라 마시는 시간
        burger = temp_burger  # 버거 개수
    elif temp_coke == coke and burger < temp_burger:  # 콜라 마시는 시간이 같을 때 최대 버거 개수
        burger = temp_burger
    cnt += 1

print('{} {}'.format(burger, coke))
