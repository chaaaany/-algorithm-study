#24-01-13 SAT
import itertools
def solution(nums):
    answer = 0
    check_num = [sum(k) for k in itertools.combinations(nums, 3)]
    for number in check_num :
        if(is_sosu(number)) :
            answer += 1
            print(number)
    return answer

def is_sosu(num) :
    for k in range(2,int(num**0.5)+1) :
        if(num % k == 0) :
            return False
    return True