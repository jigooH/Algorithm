n = int(input())

def sum_N(n) :
    if(n == 1) :
        return 1
    else :
        return n + sum_N(n - 1)
    


# 피보나치 수열
    
n = int(input())

def fibonacci(n) :
    if(n == 0) :
        return 0
    elif(n == 1) :
        return 1
    else :
        return fibonacci(n - 1) + fibonacci(n - 2)
    

# 즉, 함수를 짤때 서브함수와의 관계를 이해해야 하며 브레이크 조건을 걸어야 한다.