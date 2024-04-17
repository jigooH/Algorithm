def solution(ineq, eq, n, m):
    if eq == '=' and n == m:
        answer = 1
    if ineq == '<' and n < m:
        answer = 1
    if ineq == '>' and n > m:
        answer = 1
    answer = 0
    return answer

'''
1번 예제 계속 틀림 ("<"	"="	20	50)
질문답변안오면 멘토님한테 가져가기
'''