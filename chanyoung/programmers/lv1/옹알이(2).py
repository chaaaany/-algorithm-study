#24-01-14 SUN
def solution(babbling):
    words = [ "aya", "ye", "woo", "ma"]
    answer = 0
    for bab in babbling :
        for word in words :
            if(word*2 not in bab) : #두단어이상중복x.
                bab = bab.replace(word, '1')
        if(bab.isdigit()) : 
            answer += 1
    return answer

## 가장 먼저 떠오르는 답만이 최적은 아님.
## 콤비네이션, 퍼뮤네티션 외에 문자열로 시간복잡도 줄일 수 잇는 방법 고민.