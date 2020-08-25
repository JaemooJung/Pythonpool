import random
r_num = random.randint(1,100)    
def kr_count(i):
    if i == 1:
        kr = '한'
        return kr
    if i == 2:
        kr = '두'
        return kr
    if i == 3:
        kr = '세'
        return kr
    if i == 4:
        kr = '네'
        return kr
    if i == 5:
        kr = '다섯'
        return kr
    if i == 6:
        kr = '여섯'
        return kr
    if i == 7:
        kr = '일곱'
        return kr
    if i == 8:
        kr = '여덟'
        return kr
    if i == 9:
        kr = '아홉'
        return kr
    if i == 10:
        kr = '열'
        return kr    
for i in range(1,11):
    in_num = int(input('1부터 100 사이의 숫자를 맞추세요:'))
    if in_num < r_num:
        print('낮음!')
    elif in_num > r_num:
        print('높음!')
    elif in_num == r_num:
        print('축하합니다! 정답입니다.', kr_count(i), '번만에 맞추셨습니다.')
        break
    if i == 10 and in_num != r_num:
        print('기회가 끝났습니다! :( 정답은', r_num ,'입니다.')
        break
    print('남은 기회:', (10-i),'번')