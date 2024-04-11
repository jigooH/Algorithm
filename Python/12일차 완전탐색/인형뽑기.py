# https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3

def solution(board, moves):
    answer = 0  # 인형이 사라지는 횟수를 저장하는 변수
    basket = []  # 크레인으로 집은 인형을 담는 바구니
    
    # moves 배열의 각 원소에 대해 반복
    for move in moves:
        move -= 1  # 실제 인덱스는 0부터 시작하므로 1을 빼줌
        
        # 해당 열에서 가장 위에 있는 인형 찾기
        for i in range(len(board)):
            if board[i][move] != 0:  # 인형이 있는 경우
                # 바구니에 넣기
                if len(basket) > 0 and basket[-1] == board[i][move]:  # 바구니가 비어있지 않고, 집은 인형이 바구니 맨 위에 있는 경우
                    basket.pop()  # 바구니 맨 위의 인형을 제거하고
                    answer += 2  # 사라진 인형 개수를 2 증가시킴 (짝을 이루어서 사라진 것이므로)
                else:
                    basket.append(board[i][move])  # 바구니에 인형 추가
                board[i][move] = 0  # 인형을 뽑았으므로 해당 칸은 비게 됨
                break  # 인형을 찾았으므로 더 이상 반복할 필요 없음
    
    return answer
