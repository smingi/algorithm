# 백준 1107_리모컨


N = int(input())  # N: 이동하려고 하는 채널
M = int(input())  # M: 고장난 버튼 개수
broken = []
if M:
    broken = list(input().split())  # 고장난 버튼 리스트

minv = abs(N - 100)  # 최소 클릭 횟수

for nums in range(1000001):  # 완전탐색
    check = True  # 유효한 숫자인지 확인
    for num in str(nums):
        if num in broken:
            check = False
            break
    if check:
        minv = min(minv, abs(N-nums) + len(str(nums)))

print(minv)
