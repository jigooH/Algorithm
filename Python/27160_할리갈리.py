N = int(input())
fruit_S = {'STRAWBERRY' : 0, 'BANANA' : 0, 'LIME' : 0, 'PLUM' : 0}

for i in range(N) :
    S, count = input().split()
    fruit_S[S] += int(count)  # 밸류값 += 카운트 숫자

if 5 in fruit_S.values() :  # 밸류값에 5가 있다면
    print('YES')
else :
    print('NO')