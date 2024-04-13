'''
그리디 문제
1. 회의 시간 정렬하고
2. 순회하면서 현재 회의 시간이 이전 회의 종료시간보다 늦거나 같은거 선택

리스트 순회로만 풀어서 시간복잡도 낮음?
'''

N = int(input())
time = []

for _ in range(N):
    start, end = map(int, input().split())  # 시작시간, 끝나는 시간
    time.append((start,end))

# 끝나는 시간 기준으로 오름차순 정렬 / 같으면 시작시간 기준으로 오름차순 정렬
time.sort(key=lambda x: (x[1], x[0]))

cnt = 0  # 회의 갯수
endtime = 0  # 끝나는 시간

for i in time:
    if i[0] >= endtime:  # 현재 회의의 시작 시간이 이전 회의의 끝나는 시간보다 늦거나 같으면
        endtime = i[1]  # 끝나는 시간 갱신
        cnt += 1  # 회의시간 증가
        
print(cnt)
