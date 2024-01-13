#24-01-13 SAT
def solution(answers):
    result = []
    score = [0, 0, 0]
    answer_1 = [1, 2, 3, 4, 5]
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for idx, ans in enumerate(answers) :
        if(answer_1[idx % len(answer_1)] == ans) :
            score[0] += 1
        if(answer_2[idx % len(answer_2)] == ans) :
            score[1] += 1
        if(answer_3[idx % len(answer_3)] == ans) :
            score[2] += 1
    for idx, s in enumerate(score) :
        if s == max(score) :
            result.append(idx+1)
    return result