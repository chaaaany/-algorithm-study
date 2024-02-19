#24-01-13 SAT
def solution(k, m, score):
    score.sort(reverse = True)
    answer = 0
    for idx in range(m-1, len(score), m) :
        answer += score[idx] * m
    return answer