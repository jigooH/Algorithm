N, K = map(int, input().split())
heights = list(map(int, input().split()))

diffs = [heights[i+1] - heights[i] for i in range(N-1)]
diffs.sort()

cost = diffs[:N-K]
print(cost)
print(sum(cost))

# 출력 초과가 뜬다...