# 백준 1541_잃어버린 괄호


nums = input().split("-")  # 입력 받은 수식을 "-" 기준으로 분리

minv = sum(list(map(int, nums[0].split("+"))))  # 시작점값 구하기

for i in range(1, len(nums)):  # 계산
    minv -= sum(list(map(int, nums[i].split("+"))))

print(minv)
