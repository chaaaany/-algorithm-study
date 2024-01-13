#23-01-16 SAT
def solution(n):
    answer = 1
    for number in range(3, n+1, 2)  :
        if(is_sosu(number)) :
            answer += 1
    return answer

def is_sosu(num) :
    for k in range(2,int(num**0.5)+1) :
        if(num % k == 0) :
            return False
    return True