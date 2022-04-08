# swea 5948. 새샘이의 7-3-5 게임


def find_numbers(k, cnt, sumv):
    if cnt == 3:  # 3개 선택
        if sumv not in nums:
            nums.append(sumv)

    if k > 6:  # 인덱스 제한
        return

    find_numbers(k+1, cnt+1, sumv+numbers[k])
    find_numbers(k+1, cnt, sumv)


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    nums = []  # 숫자 조합
    find_numbers(0, 0, 0)
    nums.sort(reverse=True)
    print('#{} {}'.format(tc, nums[4]))
