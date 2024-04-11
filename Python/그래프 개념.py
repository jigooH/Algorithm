# n = 4       # 전체 노드의 갯수
# graph = [[False] * n for _ in range(n)]         # 그래프 초기 설정
# graph[0][2] = True      # 0번 노드에서 2번 노드로 가는 간선이 존재한다



'''

'''
from heapq import *

N, H, T = map(int, input().split())

# 낮은순 정렬
H.sort()

heap = []
for h in H:
    if h < T:  # 키가 T보다 작을 때
        heappush(heap, -h)  # 최대 힙 : 음수
    else:  # 키가 T 이상일때
        break

# 가장 큰 키를 T로 만들 수 없을 때
if not heap:
    print("YES\n0")
else:
    attempts = 0  # 시도 횟수
    while heap:  # 힙이 빌때까지 루프
        tallest = -heappop(heap)  # 가장 큰 키 : 다시 양수로 변환해야 해서 - 붙임
        if tallest < T:  # 가장 큰 키가 T보다 작을 때
            print("YES\n", attempts)
            break
        elif tallest == T:  # 가장 큰 키가 T와 같을 때
            print("NO")
            break
        else:  # 가장 큰 키가 T보다 클 때
            tallest //= 2  # 가장 큰 키를 T로 만들기 : 2로 나눠줌
            if tallest >= T:  # 나눈 결과가 T보다 크거나 같으면
                print("NO")  # 반복문 종료
                break
            attempts += 1  # 아니면 시도 횟수 증가시키고
            heappush(heap, -tallest)  # 새로운 키 추가 : 다시 음수로!
