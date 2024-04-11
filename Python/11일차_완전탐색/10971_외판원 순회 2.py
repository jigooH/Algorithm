'''
1. 출발점에서 모든 도시를 방문하는 경로 탐색
2. 경로 탐색하면서 비용 계산하고 최소비용 업데이트
3. 이걸 모든 출발점에서 반복
'''

import sys
input = sys.stdin.readline

# start : 출발 도시 인덱스
# now : 현재 도시 인덱스
# value : 현재까지 비용
# cnt : 현재까지 방문한 도시 수
def dfs(start, now, value, cnt):
    global ans      # ans를 전역변수로 설정(global)
    if cnt == N:
        if a[now][start]:       # [now]에서 [start]까지의 비용
            value += a[now][start]
            if ans > value:         # 최소비용이 현재까지 비용보다 크면
                ans = value         # 최소비용 갱신
        return

    if value > ans:     # 현재 비용이 최소비용보다 크면 종료
        return

    for i in range(N):
        if not visited[i] and a[now][i]:        # i를 방문하지 않았고 현재도시에서 i로 이동가능할 때
            visited[i] = 1      # 방문 표시

            # (출발 도시 인덱스, i 도시 인덱스, 현재 도시에서 i 도시까지의 비용, 방문한 도시 수 + 1)
            dfs(start, i, value + a[now][i], cnt + 1) 
            visited[i] = 0      # 방문 초기화

N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]      # 이동비용 이차원리스트
ans = sys.maxsize       # 최소 비용을 max값으로 초기화
visited = [0] * N

for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)     # 모든 도시를 출발 도시로 설정
    visited[i] = 0

print(ans)