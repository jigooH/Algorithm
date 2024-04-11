from sys import stdin
input = stdin.readline

N = int(input())
building = []
result = 0
for i in range(N):
    x, y = map(int, input().split())
    building.append(y)

stack = [0]
for i in building:
    height = i
    while stack[-1] > i:
        if stack[-1] != height:
            result += 1
            height = stack[-1]
        stack.pop()
    stack.append(i)

for _ in range(len(stack) - 1):     # 마지막 건물 팝으로 처리
    if stack[-1] != stack[-2]:
        result += 1
    stack.pop()

print(result)
