from heapq import *
from sys import stdin

input = stdin.readline

N = int(input())

heap = []

for _ in range(N):
    a = int(input())
    if a > 0:               # 파이썬에서 값이 존재할때는 a: 로만 표기해도 됨
        heappush(heap, a)   # 여기서는 자연수일때를 의미
    else:                   # a가 0일때
        if heap:            # 마찬가지로 heap이 있는지 없는지
            print(heappop(heap))
        else:
            print(0)