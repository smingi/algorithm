# 백준 7662_이중 우선순위 큐

import sys
import heapq

T = int(input())

for _ in range(T):
    k = int(input())  # k: 연산 개수
    is_pop = [False] * 1000000  # pop 여부
    max_heap = []  # 최대힙
    min_heap = []  # 최소힙

    for i in range(k):
        command, number = sys.stdin.readline().split()  # commnad: 입/출력, number: 숫자
        number = int(number)

        if command == "I":  # 삽입 연산
            heapq.heappush(max_heap, (-number, i))
            heapq.heappush(min_heap, (number, i))

        else:
            if number == 1:  # 최댓값 삭제
                while max_heap and is_pop[max_heap[0][1]]:  # min_heap 에서 뺸 부분 제거
                    heapq.heappop(max_heap)
                if max_heap:
                    is_pop[max_heap[0][1]] = True  # 뺸 부분 표시
                    heapq.heappop(max_heap)  # 최댓값 삭제
            else:  # 최솟값 삭제
                while min_heap and is_pop[min_heap[0][1]]:  # max_heap 에서 뺸 부분 제거
                    heapq.heappop(min_heap)
                if min_heap:
                    is_pop[min_heap[0][1]] = True  # 뺸 부분 표시
                    heapq.heappop(min_heap)  # 최솟값 삭제

    while max_heap and is_pop[max_heap[0][1]]:  # min_heap 에서 뺸 부분 제거
        heapq.heappop(max_heap)
    while min_heap and is_pop[min_heap[0][1]]:  # max_heap 에서 뺸 부분 제거
        heapq.heappop(min_heap)

    if max_heap and min_heap:  # 값이 남아 있는 경우
        print("{} {}".format(-max_heap[0][0], min_heap[0][0]))
    else:  # 값이 없는 경우
        print("EMPTY")
