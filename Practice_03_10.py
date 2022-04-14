x, y = map(int, input("두 정수를 입력하시오 : ").split())
if x % y == 0:
    print("{0}는(은) {1}의 배수입니다.".format(x, y))
elif x % y != 0:
    print("{0}는(은) {1}의 배수가 아닙니다.".format(x, y))

