from sys import stdin

input = stdin.readline

from collections import defaultdict

N = int(input())
len_word_mapper = defaultdict(set)  # 중복 제거를 위해 set 사용
for _ in range(N):
    word = input()
    len_word_mapper[len(word)].add(word)        # 같은 길이를 가지는 단어끼리 한 set에 묶여있도록

keys = list(len_word_mapper.keys())     # key = 단어의 길이
keys.sort()
for key in keys:
    words = list(len_word_mapper[key])      # sort를 사용하려면 set이 아닌 list 구조여야 함
    words.sort()
    for word in words:
        print(word)



# lamda 펑션으로 구현

N = int(input())
words = {input() for _ in range(N)}     # 중복 제거를 위해 set으로 생성, 인풋을 N번 받아와서 set에 넣어준다(for문)
words = list(words)     # 정렬을 위해 lsit로 변환(sort)
words.sort(key = lambda x : (len(x), x))    # 1차로 길이 순으로 정렬(len), 길이가 같다면 2차로 사전 순으로 정렬(x)
for word in words:
    print(word)