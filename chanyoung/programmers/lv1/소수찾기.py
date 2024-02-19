#23-01-16 SAT
def solution(number, limit, power):
    answer = []
    for num in range(1, number+1) :
        tmp = 0
        for k in range(1, int(num ** 0.5)+1) :
            if(num % k == 0) :
                tmp += 1
        if((num ** 0.5) **  2 == num) :
            if(tmp*2-1 > limit) :
                answer.append(power)
            else : 
                answer.append(tmp*2 -1)
        else : ## 제곱수가 아니면
            if(tmp*2 > limit) :
                answer.append(power)
            else : 
                answer.append(power)
    return sum(answer)
print()