N = int(input())
times = list(map(int, input().split()))
times.sort()
result = 0
waiting = 0

for time in times:
    waiting += time
    result += waiting
print(result)