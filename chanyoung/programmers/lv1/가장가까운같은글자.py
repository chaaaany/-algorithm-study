#24-01-13 SAT
def solution(s):
    answer = []
    for i in range(len(s)) : 
        if(s[i] in s[0:i]) :
            answer.append(i - s[0:i].rindex(s[i]))
        else : 
            answer.append(-1)
    return answer

#rindex() : 뒤에서부터 찾아서 반환. (<-> index())