from sys import stdin

input = stdin.readline

N = int(input())
sources = list(map(int, input().split()))
visited = {}
for source in sources:
    visited[source] = 1

M = int(input())
targets = list(map(int, input().split()))
for target in targets:
    print(visited.get(target, 0))       # get 함수는 target이라는 키가 없을 때 디폴트값을 반환
                                        # 있다면 1을 반환, 없다면 0을 반환


                                        # 이분 탐색으로 풀어보기(딱히 좋은 풀이는 아님)

                                    
def search(arr, t):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == t:
            return True
        elif arr[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    return False

N = int(input())
sources = list(map(int, input().split()))
sources.sort()      # 이분 탐색을 하려면 반드시 정렬이 되어야
M = int(input())
targets = list(map(int, input().split()))
for target in targets:
    print(1 if search(sources, target) else 0)