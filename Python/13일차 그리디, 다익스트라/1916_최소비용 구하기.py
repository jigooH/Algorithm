'''
전형적인 다익스트라 문제
이거무조건해야됨 다익스트라 공짜로 먹고 갈려면 이거랑 4번 풀기
처음하면 정상인데 암튼 악으로 깡으로 풀기
'''


import sys
from heapq import *

def dijkstra(start, end, graph):
    # 시작 도시부터 각 도시까지의 최소 비용을 저장할 리스트
    cost = [float('inf')] * (N + 1)  # 모든 도시까지의 비용을 무한대로 초기화
    cost[start] = 0  # 시작 도시까지의 비용은 0으로 설정
    
    queue = []  # 우선순위 큐 초기화
    heappush(queue, (0, start))  # 시작 도시의 비용을 0으로 설정 / 우선순위 큐에 삽입

    while queue:
        current_cost, current_city = heappop(queue)  # 현재까지의 비용 / 현재 도시를 우선순위 큐에서 꺼냄

        if cost[current_city] < current_cost:  # 현재까지의 비용이 저장된 비용보다 크면 무시
            continue

        for next_city, next_cost in graph[current_city]:  # 현재 도시에서 이동할 수 있는 모든 도시들을 반복
            new_cost = current_cost + next_cost  # 새로운 비용은 현재까지의 비용에 현재 도시에서 다음 도시로 가는 비용을 더한 값

            if new_cost < cost[next_city]:  # 새로운 비용이 기존에 저장된 비용보다 작으면
                cost[next_city] = new_cost  # 해당 도시까지의 최소 비용을 업데이트하고
                heappush(queue, (new_cost, next_city))  # 우선순위 큐에 새로운 도시와 비용을 삽입, 다음 탐색 진행

    return cost[end]  # 목적지 도시까지의 최소 비용 반환



N = int(sys.stdin.readline().strip())  # 도시 개수
M = int(sys.stdin.readline().strip())  # 버스 개수

bus_info = [[] for _ in range(N + 1)]  # 각 도시에서 출발하는 버스 정보 리스트 초기화

# 각 도시에서 출발하는 버스 정보를 입력받아 리스트에 저장
for i in range(M):
    start_city, end_city, cost = map(int, sys.stdin.readline().strip().split())
    bus_info[start_city].append((end_city, cost))

start, end = map(int, sys.stdin.readline().strip().split())  # 출발 도시와 도착 도시 입력

min_cost = dijkstra(start, end, bus_info)

print(min_cost)