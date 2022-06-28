import sys
import heapq

N = int(input())

left = []  # 왼쪽 힙(작은수 리스트) - 최대 힙
right = []  # 오른쪽 힙(큰수 리스트) - 최소 힙

for i in range(N):
    num = int(sys.stdin.readline())  # 들어온 숫자
    
    if len(left) == len(right):
        heapq.heappush(left, -num)  # heapq는 최소 힙만 가능(-로 최대 힙으로 만들기)
    else:
        heapq.heappush(right, num)

    if right and -left[0] > right[0]:  # 왼쪽 힙에는 오른쪽 힙보다 작은 값만 들어오도록 조정
        left_maxv = -heapq.heappop(left)
        right_minv = heapq.heappop(right)

        heapq.heappush(left, -right_minv)
        heapq.heappush(right, left_maxv)

    print(-left[0])  # 왼쪽 힙의 최상단 값이 중간값이 됨
