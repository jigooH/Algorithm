from heapq import *
from sys import stdin

input = stdin.readline


'''
최소 힙 개념만 존재.
최대 힙을 구하려면 -를 붙여서 음수로 바꿔야 함
'''

a = [5, 4, 3, 1, 2]     # 일반 리스트 생성
heapify(a)              # a를 최소 힙으로 변환
print(a[0])             # 1
print(heappop(a))       # 최솟값 추출 -> 1
print(a[0])             # 2
heappush(a, 7)          # 힙에 7을 추가
print(a[0])             # 2
heappush(a, 0)
print(a[0])             # 0