#23-01-13
def solution(s):
    result = ''
    num_dict = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    for key in num_dict :
        s = s.replace(key, num_dict[key])
    return int(s)