N = int(input("정수를 입력하시오 : "))

if(N % 2 == 0):
    print("{0}는 2로 나누어집니다.".format(N))
if(N % 2 != 0):
    print("{0}는 2로 나누어지지 않습니다.".format(N))
if(N % 3 == 0):
    print("{0}는 3로 나누어집니다.".format(N))
if(N % 3 != 0):
    print("{0}는 3로 나누어지지 않습니다.".format(N))
if(N % 2 == 0 and N % 3 == 0):
    print("{0}는 2와 3 모두로 나누어집니다.".format(N))
if(N % 2 != 0 or N % 3 != 0):
    print("{0}는 2와 3 모두로 나누어지지 않습니다.".format(N))

