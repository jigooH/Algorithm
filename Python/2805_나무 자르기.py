'''
1. 나무 키 오름차순으로 정렬
2. 자를 범위 이분탐색(0부터 제일 높은 나무)
3. 자르고 남은 길이 계산
4. 남은 길이가 M보다 크거나 같으면 mid + 1
5. 작으면 mid - 1
'''

from sys import stdin
input = stdin.readline

def total_length(trees, height):                    # 잘린 부분 계산(총합)
    total = 0
    for tree in trees:
        if tree > height:
            total += tree - height
    return total

def binary_search(trees, target_length):            # 자르는 지점 최대 높이를 이분 탐색
    left= 0
    right = max(trees)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        length = total_length(trees, mid)
        if length >= target_length:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


N, M = map(int, input().split())
trees = list(map(int, input().split()))
answer = binary_search(trees, M)                # 이분탐색 함수값 할당
print(answer)