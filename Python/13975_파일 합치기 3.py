from sys import stdin
from heapq import *
input = stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())        # 파일 갯수
    file = list(map(int, input().split()))      # 파일 크기
    heapify(file)       # 리스트를 힙으로 변환
    result = 0      # 총비용

    while len(file) > 1:        # 파일이 1개가 되면 종료
        small_1 = heappop(file)       # 가장 작은 두 개의 파일 크기
        small_2 = heappop(file)
        result += small_1 + small_2     # 를 더함
        heappush(file, small_1 + small_2)       # 파일 크기를 힙에 추가

    print(result)