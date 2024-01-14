
#24-01-14 SUN
def solution(number, limit, power):
    answer = []
    for num in range(1, number+1) :
        tmp = 0
        for k in range(1, int(num ** 0.5)+1) :
            if(num % k == 0) :
                tmp += 1
        if((num ** 0.5) == int(num ** 0.5)) :
            if(tmp*2-1 > limit) :
                answer.append(power)
            else : 
                answer.append(tmp*2 -1)
                
        else : ## 제곱수가 아니면
            if(tmp*2 > limit) :
                answer.append(power)
            else : 
                answer.append(tmp*2)
    return sum(answer)

print(solution(20, 100, 0))
#지저분하긴한데 다른 아이디어도 그닥...
