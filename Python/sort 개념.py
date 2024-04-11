'''
파이썬에서는 sort 함수를 제공한다.
Python list에 대해 사용할 수 있는 함수로, 반환값 없이 list를 오름차순으로 정리해 준다.
'''

a = {2, 3, 1, 4}
a.sort()            # 반환값 없음
print(a)            # {1, 2, 3, 4}

a.sort(reversed=True)   # a를 내림차순 정렬
print(a)                # {4, 3, 2, 1}


'''
오름차순, 내림차순 정렬은 이렇게 하면 됨
근데 내가 원하는 특별한 기준으로 정렬하고 싶을 때는?
'''

a = [2, -1, 4, -3]
a.sort(key = lambda x : x * x)      # x의 제곱 값을 기준으로 오름차순 정렬
print(a)    # [-1, 2, -3, 4]

a.sort(key = lambda x : x * x, reverse = True)       # key / reverse 같이 사용할 수 있음!
print(a)            # [4, -3, 2, -1]