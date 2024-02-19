#24-01-13 SAT
def solution(strings, n):
    return sorted(strings, key = lambda x:(x[n], x))

#lambda 매개변수 : 표현식
#sorted key는 튜플로 우선순위 지정 가능
#https://wikidocs.net/64 참고하기