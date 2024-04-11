import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, N + 1):
    combi = combinations(arr, i)  # 콤비네이션 함수 : arr 배열에서 길이가 i인 모든 조합 반환
    for j in combi:
        if sum(j) == S:  # 부분 집합의 합이 목표 합과 같은지 확인
            cnt += 1  # 부분 집합의 합이 목표 합과 같으면 카운터 증가

# 결과 출력
print(cnt)