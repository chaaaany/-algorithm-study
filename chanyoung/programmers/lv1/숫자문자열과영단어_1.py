#24-01-13
#기존코드
def solution(s):
    result = ''
    num_dict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tmp = ''
    for letter in s : 
        if(letter.isdigit()) :
            result += letter
        else :
            tmp += letter
            if tmp in num_dict :
                result += str(num_dict.index(tmp))
                tmp = ''
    return int(result)
