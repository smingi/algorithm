# 백준 2839 설탕 배달

n = int(input())
result = -1  # 결과값
cnt = 0  # 3kg 포대 수
if n % 5 == 0:
    result = n//5  # 5로 나누어지면 5로 나누어진 값이 최소개수
else:
    temp = n  # 원래 n값이 변경되지 않도록 temp에 n의 값을 저장
    while cnt <= n//3:  # 3kg 포대만으로 구성해도 수가 안맞을 때까지
        cnt5 = (temp - 3*cnt)//5  # 5kg 포대의 개수는 전체개수에서 3kg 수를 빼고 5로 나눈 값
        if cnt5 < 0:
            cnt5 = 0  # 12번째 줄 식 때문에 5kg 포대 개수가 음수가 되면 cnt5를 0으로 고정시켜야함
        res = temp - (cnt5*5)  # 5kg 포대 무게를 뺀 나머지
        if res % 3 == 0:  # 나머지가 3으로 나누어지면 나머지를 3으로 나누고 cnt5값을 더함
            result = cnt5 + res//3
            break
        else:  # 3으로 안나누어지면 3kg 포대 양을 늘림
            cnt += 1

print(result)