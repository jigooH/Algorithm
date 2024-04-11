'''
이분 탐색은 정렬된 배열에서, 원하는 값을 빠르게 찾는 탐색 방법이다.

1부터 100까지의 값 중에서 하나를 고르고, 고른 값을 맞추는 게임을 생각해 보자.
숫자를 말하면 말한 숫자보다 정답이 큰지 작은지 알려준다.

만약 1부터 100까지 차례대로 숫자를 물어본다면 최대 100번의 질문을 해야 한다.
하지만 50 -> 25 -> 12 ... 와 같이 탐색 범위를 줄여나간다면 최대 7번의 질문으로 해결 가능하다.

정렬된 배열에서, 탐색 범위를 절반씩 줄여나가는 탐색 방법을 이분 탐색이라고 한다.
절반씩 줄여나가면서 탐색 범위가 1이 될 때까지 진행하므로 시간 복잡도는 O(logn)이다. 이진 탐색이라고도 불린다.
'''

# 정수 리스트 arr 안에 target이 있으면 그 인덱스를, 없으면 -1을 반환하는 함수를 작성해보자.

def binary_search(arr : list[int], target : int):
    left = 0                # 첫 변수
    right = len(arr) - 1    # 마지막 변수

    while left <= right :
        mid = (left + right) // 2
        if arr [mid] == target :
            return mid
        elif  arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1               # not found