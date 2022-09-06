# 백준 1202_보석 도둑

import sys
import heapq


N, K = map(int, sys.stdin.readline().split())  # N: 보석의 개수, K: 가방의 개수
jewel = []  # 보석(무게, 가격)
for _ in range(N):
    heapq.heappush(jewel, list(map(int, sys.stdin.readline().split())))

bag = [int(sys.stdin.readline()) for _ in range(K)]  # 가방(무게 제한)
bag.sort()  # 용량 작은순으로 정렬

heap = []
max_value = 0  # 가장 큰 가치

for b in bag:
    while jewel and b >= jewel[0][0]:  # 가방에 넣을 수 있는 보석을 모두 찾기
        heapq.heappush(heap, -jewel[0][1])  # 낮은 heap 만 지원하기 때문에 최대값을 저장하기 위해 음수로 저장
        heapq.heappop(jewel)  # 넣은 보석은 빼기

    if heap:  # 넣을 수 있는 보석 중 가장 가치가 높은 보석 선택
        max_value -= heapq.heappop(heap)  # 음수로 저장했기 때문에 뺄샘으로 저장

    elif not jewel:
        break

print(max_value)  # 가장 큰 가치 출력
