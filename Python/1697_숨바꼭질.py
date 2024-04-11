'''
BFS 문제같은데 개념을 전혀 이해하지 못해서 다른 방식으로 풀려다가 런타임 에러가 났습니다...
입출력값도 안맞는데 푼 시간이 아까워서 일단 올려봅니다
'''

N, K = map(int, input().split())
max_size = 100001       # 최대 크기 설정
start = [max_size] * max_size       # 리스트 초기화
start[N] = 0

for i in range(N, K + 1):
    start[i + 1] = min(start[i + 1], start[i] + 1)      # 1을 더하는 경우
    start[i * 2] = min(start[i * 2], start[i] + 1)      # 2배인 경우
    if i > 0:       # 1을 빼는 경우
        start[i - 1] = min(start[i - 1], start[i] + 1)

print(start[K])