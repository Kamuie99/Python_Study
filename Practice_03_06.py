# 3개의 정수를 입력받아 가장 작은수 부터 나열

a, b, c = map(int, input("세 정수를 입력하시오 : ").split())


if min(a, b, c) == a:
    if b <= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif min(a, b, c) == b:
    if a <= c:
        print(b, a, c)
    else:
        print(b, c, a)
elif min(a, b, c) == c:
    if a <= b:
        print(c, a, b)
    else:
        print(c, b, a)


