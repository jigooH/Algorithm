from itertools import combinations

N = int(input())
scoreboard = [list(map(int, input().split())) for _ in range(N)]

team_with_0s = list(combinations(range(1, N), N // 2 - 1))      # 0번 사람 + (N // 2 - 1)명으로 팀을 구성
M = float('inf')        # 무한대. 최솟값을 찾을 때 초기값으로 사용하면 편함

for team1 in team_with_0s:
    team1 = [0] + list(team1)
    team2 = list(set(range(N)) - set(team1))
    score1 = 0
    score2 = 0
    for i in range(N // 2):
        for j in range(N // 2):
            score1 += scoreboard[team1[i]][team1[j]]
            score2 += scoreboard[team2[i]][team2[j]]
    M = min(M, abs(score1 - score2))

print(M)