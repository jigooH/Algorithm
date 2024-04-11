N = int(input())
switch = list(map(int, input().split()))
change = {1: 0, 0: 1}

for _ in range(int(input())):
    gender, num = map(int, input().split())
    i = 1
    if gender == 1:
        while num * i - 1 < N:
            switch[num * i - 1] = change[switch[num * i - 1]]
            i += 1
    elif gender == 2:
        switch[num - 1] = change[switch[num - 1]]
        while 1 <= num - i and num + i < N + 1 and switch[num - i - 1] == switch[num - 1 + i]:
            switch[num - 1 - i] = change[switch[num - 1 - i]]
            switch[num - 1 + i] = change[switch[num - 1 + i]]
            i += 1

for i in range(N):
    print(switch[i], end=" ")
    if i % 20 == 19:
        print()