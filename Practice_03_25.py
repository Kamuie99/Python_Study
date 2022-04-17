d = 0
m = 0

while 1:
    m += 7
    d += 1
    if m >= 30:
        print("day : {0} 달팽이의 위치 : {1} 미터".format(d, m))
        print("우물을 탈출하는 데 걸린 날은 {0}일 입니다.".format(d))
        break
    else:
        m -= 5
        print("day : {0} 달팽이의 위치 : {1} 미터".format(d, m))

